from django.shortcuts import render, redirect
from .models import Sucursales
from Sucursales.forms import SucursalesForm

def index(request):
    return render(request, "Sucursales/index.html")

def lista_sucursales(request):
    consulta = Sucursales.objects.all()
    contexto = {"Sucursales": consulta}
    return render(request, "Sucursales/lista_sucursales.html", contexto)

def sucursal_create(request):
    if request.method == "POST":
        form = SucursalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Sucursales:lista_sucursales")
    else: #GET
        form = SucursalesForm()
    return render(request, "Sucursales/sucursales_form.html", {"form": form})