from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("<h1>Ejemplo de la app2 vista 2 1 </h1>")