from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Persona, Sexo, Ciudad
from datetime import datetime

from .forms import Personaforms

# Creación de las views.

def Index(request):

    return render(request, "index.html", {})

def Login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('turnero')
        else:
            return render(request, 'login.html', {'error': 'Las credenciales introducidas son invalidas'})

    return render(request, 'login.html')

def Persona_views(request):
    form = Personaforms(request.POST or None)
    POST_data = request.POST  # Obtener los datos del POST

    persona_cedula = request.POST.get("persona_cedula")
    persona_nombre = request.POST.get("persona_nombre")
    persona_apellido = request.POST.get("persona_apellido")
    persona_fecha_nacimineto = request.POST.get("persona_fecha_nacimineto")
    sexo_id = request.POST.get("sexo_id")
    ciudad_id = request.POST.get("ciudad_id")
    persona_direccion = request.POST.get("persona_direccion")
    persona_telefono = request.POST.get("persona_telefono")
    persona_correo = request.POST.get("persona_correo")

    print('FECHA NACIMIENTO:')
    print(persona_fecha_nacimineto)

    if POST_data:
        obj = Persona()
        obj.persona_cedula = persona_cedula
        obj.persona_nombre = persona_nombre
        obj.persona_apellido = persona_apellido
        obj.sexo_id = Sexo.objects.get(sexo_id=sexo_id)
        obj.persona_fecha_nacimineto = datetime.strptime(persona_fecha_nacimineto, "%d/%m/%Y").strftime("%Y-%m-%d")
        obj.ciudad_id = Ciudad.objects.get(ciudad_id=ciudad_id)
        obj.persona_direccion = persona_direccion
        obj.persona_telefono = persona_telefono
        obj.persona_correo = persona_correo
        obj.save()
        messages.success(request, 'Cliente registrado correctamente.')

    context = {
        "form": Personaforms(),
        "titulo": "AgregarPersona"
    }

    return render(request, 'persona.html', context)

    # if form.is_valid():
    #     if POST_data:

    # if request.method=='POST':
    #     return redirect(request,'persona')

def Servicio_views(request):

    return redirect('turnero')

def Turnos_views(request):

    return redirect('turnero')

def ListaServicios_views(request):

    return redirect('turnero')

