from django.contrib import admin
from . import models

# Registro de los modelos:

admin.site.register(models.Pais)

admin.site.register(models.Departamento)

admin.site.register(models.Ciudad)

admin.site.register(models.Empresa)

admin.site.register(models.Parametro)

admin.site.register(models.Permiso)

admin.site.register(models.Rol)

admin.site.register(models.Sexo)

admin.site.register(models.Persona)

admin.site.register(models.TipoPersona)

admin.site.register(models.PersonaSet)

admin.site.register(models.Servicio)

admin.site.register(models.Usuario)

admin.site.register(models.NivelPrioridad)


admin.site.register(models.Cola)

admin.site.register(models.Ticket)
