from django.shortcuts import render
from . import models

def index(request):
    consulta = models.Clientes.objects.all()
    contexto = {"clientes": consulta}
    return render(request, "Clientes/index.html", contexto)