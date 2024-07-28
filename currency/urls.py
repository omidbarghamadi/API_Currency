from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CurrencyList.as_view()),
]