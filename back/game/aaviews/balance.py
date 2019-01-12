from rest_framework import generics

from ..models import Balance
from ..serializers import BalanceSerializer


class ListBalance(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class DetailBalance(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
