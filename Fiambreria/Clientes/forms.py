from django import forms
from . import models

class ClientesForm(forms.ModelForm):
    class Meta:
        model = models.Clientes
        fields = ["nombre", "apellido", "email", "sucursal"]