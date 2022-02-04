from django.db import models
from clients.models import Client
from products.models import Product


class Bill(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    nit = models.CharField(max_length=50)
    code = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='billsproducts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name