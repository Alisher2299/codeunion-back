from rest_framework import generics
from .models import Currency
from .serializers import CurrencySerializer
from common.pagination import CustomPagination


class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = CustomPagination


class CurrencyDetail(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
