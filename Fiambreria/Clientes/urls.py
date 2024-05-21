from django.urls import path
from Clientes.views import index, lista_clientes, cliente_create

app_name = "Clientes"
urlpatterns = [
    path("", index, name="index"),
    path("Listado", lista_clientes, name="lista_clientes"),
    path("create", cliente_create, name="clientes_create"),
]