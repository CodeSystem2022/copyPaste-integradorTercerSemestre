from django.shortcuts import render

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
