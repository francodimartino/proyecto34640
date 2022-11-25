
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("curso/", curso, name="curso"),
    path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path("", inicio, name="inicio"),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),

]