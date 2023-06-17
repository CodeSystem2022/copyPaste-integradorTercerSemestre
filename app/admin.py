from django.contrib import admin
from . import models

# Registro de los modelos:

admin.site.register(models.Pais)

admin.site.register(models.Departamento)

admin.site.register(models.Ciudad)
