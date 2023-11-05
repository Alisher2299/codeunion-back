from django.urls import path
from .views import CurrencyList, CurrencyDetail

urlpatterns = [
    path('currencies', CurrencyList.as_view(), name='currency-list'),
    path('currency/<int:pk>', CurrencyDetail.as_view(), name='currency-detail'),
]
