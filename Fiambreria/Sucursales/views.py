from django.shortcuts import render
from .models import Sucursales

def index(request):
    return render(request, "Sucursales/index.html")

def lista_sucursales(request):
    consulta = sucursal.objects.all()
    contexto = {"sucursal": consulta}
    return render(request, "Sucursales/lista_sucursales.html", contexto)