from django.db import models


class Sucursales(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    direccion = models.CharField(
        max_length=200
        )

    def __str__(self) -> str:
        """Retorna una instancia del modelo en forma de cadena de texto"""
        return f"{self.nombre}, {self.direccion}"

