from django import forms
from . import models

class SucursalesForm(forms.ModelForm):
    class Meta:
        model = models.Sucursales
        fields = ["nombre", "direccion"]