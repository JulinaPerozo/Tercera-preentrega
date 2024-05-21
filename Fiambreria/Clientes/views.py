from django.shortcuts import render, redirect
from .models import Clientes
from Clientes.forms import ClientesForm

def index(request):
    return render(request, "Clientes/index.html")

def lista_clientes(request):
    consulta = Clientes.objects.all()
    contexto = {"Clientes": consulta}
    return render(request, "Clientes/lista_clientes.html", contexto)

def cliente_create(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clientes:lista_clientes.html")
    else: #GET
        form = ClientesForm()
    return render(request, "Clientes/cliente_form.html", {"form": form})