from django.urls import path
from .views import (RetrieveBillView, ListBillView, CreateBillView,
                   UpdateBillView, DestroyBillView)

app_name = "bills"
urlpatterns = [
    path("detail/<int:pk>", RetrieveBillView.as_view(), name="detail"),
    path("list/", ListBillView.as_view(), name="list"),
    path("create/", CreateBillView.as_view(), name="create"),
    path("update/<int:pk>", UpdateBillView.as_view(), name="update"),
    path("delete/<int:pk>", DestroyBillView.as_view(), name="delete"),
]
