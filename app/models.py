from django.db import models

# Creación de los modelos.

class Pais(models.Model):
    pais_id = models.AutoField(primary_key=True)
    pais_descripcion = models.CharField(max_length=25,blank=False,null=False)
    pais_abreviatura = models.CharField(max_length=3,blank=True)

    def __str__(self) -> str:
        return self.pais_descripcion


class Departamento(models.Model):
    departamento_id = models.AutoField(primary_key=True)
    pais_id = models.ForeignKey('Pais', on_delete=models.CASCADE)
    departamento_descripcion = models.CharField(max_length=25,blank=False,null=False)
    departamento_nro = models.BigIntegerField(blank=False,null=False)
    departamento_abreviatura = models.CharField(max_length=5,blank=True)

    def __str__(self) -> str:
        return self.departamento_descripcion

class Ciudad(models.Model):
    ciudad_id = models.AutoField(primary_key=True)
    departamento_id = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    ciudad_descripcion = models.CharField(max_length=25,blank=False,null=False)
    capital_dpto=models.BooleanField(default=False,blank=False,null=False)

    def __str__(self) -> str:
        return self.ciudad_descripcion
