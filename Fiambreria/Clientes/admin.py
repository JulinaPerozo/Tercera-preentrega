from django.contrib import admin

from . import models

admin.site.register(models.Clientes)
admin.site.register(models.Empleados)
admin.site.register(models.Sucursal)

