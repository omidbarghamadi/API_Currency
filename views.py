from .models import currency
from django.utils import timezone
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests

from .serializer import CurrencySerializer


class CurrencyList(APIView):
    @staticmethod
    def ExcuteApi():
        Token = 'your_token'
        Source = 'bonbast'
        try:
            url = f'https://one-api.ir/price/?token={Token}&action={Source}'
            response = requests.get(url)
            return response.json()
        except requests.Timeout or requests.ConnectionError:
            return None

    def get(self, request):
        results = []
        data = self.ExcuteApi()

        try:
            currencies = {
                'USD': data['result']['usd1'],
                'EUR': data['result']['eur1'],
                'AED': data['result']['aed1']
            }
            results = []
            i = 0
            for name, price in currencies.items():
                results.append({
                    'name': name,
                    'price': price,
                    'time': datetime.now().time(),
                    'date': timezone.now().date()
                })
                try:
                    # Update price and time with everyday
                    queryset = currency.objects.get(name=name, date=timezone.now().date())
                    serializer = CurrencySerializer(queryset, data=results[i])

                except currency.DoesNotExist:
                    # else create record
                    serializer = CurrencySerializer(data=results[i])

                i += 1
                if serializer.is_valid():
                    serializer.save()

        except Exception:
            currencies = ['USD', 'EUR', 'AED']
            for item in currencies:
                queryset = currency.objects.order_by('-date').filter(name=item).first()
                serializer = CurrencySerializer(queryset)
                results.append(serializer.data)

        return Response(results, status=status.HTTP_200_OK)
