from django.urls import path, include
from .views import (LoginClientView, RetrieveClientView, ListClientView, 
                    CreateClientView, UpdateClientView, DestroyClientView, 
                    ExportClientView, ImportClientView)

app_name = "clients"
urlpatterns = [
    path("login/", LoginClientView.as_view(), name="login"),
    path("detail/<int:pk>", RetrieveClientView.as_view(), name="detail"),
    path("list/", ListClientView.as_view(), name="list"),
    path("create/", CreateClientView.as_view(), name="create"),
    path("update/<int:pk>", UpdateClientView.as_view(), name="update"),
    path("delete/<int:pk>", DestroyClientView.as_view(), name="delete"),
    path("export/", ExportClientView.as_view(), name="export"),
    path("import/", ImportClientView.as_view(), name="import")
]
