from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

#view inicio
def inicio(request):
    return render(request, 'paginas/inicio.html')

#view nosotros
def nosotros (request):
    return render(request, 'paginas/nosotros.html')

#view CRUD libros
def libros (request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

#view crear libros
def crear (request):
    formulario = LibroForm(request.POST or None)
    return render(request, 'libros/crear.html', {'formulario': formulario})

#view editar libros
def editar (request):
    return render(request, 'libros/editar.html')