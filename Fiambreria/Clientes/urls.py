from django.urls import path
from Clientes.views import index, lista_clientes

app_name = "Clientes"
urlpatterns = [
    path("", index, name="index"),
    path("Listado", lista_clientes, name="lista_clientes"),
]