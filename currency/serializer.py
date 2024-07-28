from django.core.serializers import _load_serializers
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from datetime import datetime

from .models import currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = currency
        fields = ['name', 'price', 'time', 'date']

    def create(self, validated_data):
        return currency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.time = datetime.now().time()
        instance.save()
        return instance
