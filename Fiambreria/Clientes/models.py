from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    direccion = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.direccion}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}, {self.email}, {self.sucursal}"

class Empleados(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}, {self.sucursal}"