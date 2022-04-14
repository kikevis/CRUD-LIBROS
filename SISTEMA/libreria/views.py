from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#view inicio
def inicio(request):
    return render(request, 'paginas/inicio.html')

#view nosotros
def nosotros (request):
    return render(request, 'paginas/nosotros.html')

#view CRUD libros
def libros (request):
    return render(request, 'libros/index.html')

#view crear libros
def crear (request):
    return render(request, 'libros/crear.html')

#view editar libros
def editar (request):
    return render(request, 'libros/editar.html')