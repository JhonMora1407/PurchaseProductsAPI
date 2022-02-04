from rest_framework import serializers
from .models import Bill
from products.serializers import ProductSerializer
from clients.serializers import ClientSerializer


class BillReadSerializer(serializers.ModelSerializer):

    client_id = ClientSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = (
            'id',
            'client_id',
            'company_name',
            'nit',
            'code',
            'products',
            'created_at'
        )


class BillWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = (
            'id',
            'client_id',
            'company_name',
            'nit',
            'code',
            'products',
            'created_at'
        )
