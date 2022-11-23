from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def curso(request):

    curso1=Curso(nombre="Python",comision=34640)
    
    curso.save()
    cadena_Texto="Curso guardado: "+curso.nombre+" "+str(curso.comision)
    return HttpResponse(cadena_Texto)


def inicio(request):
    

    return render (request, "AppCoder/inicio.html")


def cursos(request):
    return render (request, "AppCoder/cursos.html")

def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")

def profesores(request):
    return render (request, "AppCoder/profesores.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")
