from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse

from AppCoder.forms import CursoForm, ProfeForm

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

    if request.method=="POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            email=informacion["email"]
            profesion=informacion["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "Appcoder/inicio.html", {"mensaje": "PROFESOR CREADO CORRECTAMENTE!!"})
    else:
        formulario=ProfeForm()


    return render (request, "AppCoder/profesores.html", {"form":formulario})

def entregables(request):
    return render (request, "AppCoder/entregables.html")

""" def cursoFormulario(request):

    if request.method=="POST":
        nombrecito=request.POST["nombre"]
        comisioncita=request.POST["comision"]

        curso1=Curso(nombre=nombrecito,comision=comisioncita)
        curso1.save()
        return render (request, "AppCoder/inicio.html")


    return render(request, "AppCoder/cursoFormulario.html") """

def cursoFormulario(request):

    if request.method=="POST":
        form=CursoForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombrecito=informacion["nombre"]
            comisioncita=informacion["comision"]

            curso1=Curso(nombre=nombrecito,comision=comisioncita)
            curso1.save()
            return render (request, "AppCoder/inicio.html")
    else:
        formulario=CursoForm()


    return render(request, "AppCoder/cursoFormulario.html", {"form":formulario})


def busquedaComision(request):
    return render(request, "Appcoder/busquedaComision.html")


def buscar(request):

    if request.GET["comision"]:

        comision=request.GET["comision"]

        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request,"Appcoder/resultadosBusqueda.html", {"cursos":cursos} )
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje":"CHE! Ingresa una comision"})








