from django.shortcuts import render, redirect
from .models import Incidencia
from .forms import FormularioIncidencias

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def listarIncidencias(request):
    incidencias = Incidencia.objects.all()
    contexto     = {'incidencias':incidencias}
    return render(request, 'ListarIncidencias.html',context=contexto)

def agregarIncidencias(request):
    if request.method == 'POST':
        formulario = FormularioIncidencias(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = FormularioIncidencias()

    contexto   ={'formulario':formulario}
    return render(request, 'AgregarIncidencias.html',context=contexto)