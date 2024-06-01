from django.urls import path
from Sucursales.views import index, lista_sucursales, sucursal_create

app_name = "Sucursales"
urlpatterns = [
    path("", index, name="index"),
    path("listado", lista_sucursales, name="lista_sucursales"),
    path("create", sucursal_create, name="create")
]