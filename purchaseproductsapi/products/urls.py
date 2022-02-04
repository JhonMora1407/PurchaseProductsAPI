from django.urls import path
from .views import (RetrieveProductView, ListProductView, CreateProductView,
                    UpdateProductView, DestroyProductView)

app_name = "products"
urlpatterns = [
    path("detail/<int:pk>", RetrieveProductView.as_view(), name="detail"),
    path("list/", ListProductView.as_view(), name="list"),
    path("create/", CreateProductView.as_view(), name="create"),
    path("update/<int:pk>", UpdateProductView.as_view(), name="update"),
    path("delete/<int:pk>", DestroyProductView.as_view(), name="delete"),
]
