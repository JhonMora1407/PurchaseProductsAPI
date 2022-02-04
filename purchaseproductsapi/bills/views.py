from rest_framework import generics
from .models import Bill
from .serializers import BillReadSerializer, BillWriteSerializer


class RetrieveBillView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillReadSerializer


class ListBillView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillReadSerializer


class CreateBillView(generics.CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillWriteSerializer


class UpdateBillView(generics.UpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillWriteSerializer


class DestroyBillView(generics.DestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillWriteSerializer
