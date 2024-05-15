from django.urls import path
from Sucursales.views import index, lista_sucursales

app_name = "Sucursales"
urlpatterns = [
    path("", index, name="index"),
    path("Sucursales", lista_sucursales, name="lista_sucursales"),
]