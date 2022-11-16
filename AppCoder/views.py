from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.


def curso(request):

    curso1=Curso(nombre="Python",comision=34640)
    
    curso.save()
    cadena_Texto="Curso guardado: "+curso.nombre+" "+str(curso.comision)
    return HttpResponse(cadena_Texto)
