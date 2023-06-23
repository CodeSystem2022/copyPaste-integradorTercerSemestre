from django import forms
from . import models
from .models import Persona


class Personaforms(forms.Form):
    persona_cedula = forms.CharField(max_length=15, required=True)
    persona_nombre = forms.CharField(max_length=50, required=True)
    persona_apellido = forms.CharField(max_length=50, required=True)
    persona_fecha_nacimieto = forms.DateField(widget=DateInput, required=False)
    sexo_id = forms.ModelChoiceField(queryset=models.Sexo.objects.all(), required=False)
    ciudad_id = forms.ModelChoiceField(queryset=models.Ciudad.objects.all(), required=False)
    persona_direccion = forms.CharField(max_length=50, required=False)
    persona_telefono = forms.CharField(max_length=15, required=False)
    persona_correo = forms.CharField(max_length=25, required=False)
