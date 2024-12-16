from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("¡Hola, mundo! Esta es mi primera vista en Django.")
