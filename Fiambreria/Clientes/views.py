from django.shortcuts import render
from .models import Clientes

def index(request):
    return render(request, "Clientes/index.html")

def lista_clientes(request):
    consulta = Clientes.objects.all()
    contexto = {"Clientes": consulta}
    return render(request, "Clientes/lista_clientes.html", contexto)