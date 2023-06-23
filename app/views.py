from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login


# Creación de las views.

def Index(request):
    """
    titulo="Turnero"
    context={
        "Titulo": titulo
    }
    return render(request,"index.html",context)
    """
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
    pass
    return redirect('turnero')

def Servicio_views(request):
    pass
    return redirect('turnero')

def Turnos_views(request):
    pass
    return redirect('turnero')

def ListaServicios_views(request):
    pass
    return redirect('turnero')

