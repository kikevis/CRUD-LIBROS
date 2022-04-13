from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#view inicio
def inicio(request):
    return render(request, 'paginas/inicio.html')

#view nosotros
def nosotros (request):
    return render(request, 'paginas/nosotros.html')