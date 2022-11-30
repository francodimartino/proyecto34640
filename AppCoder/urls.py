
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
    path("leerProfesores/", leerProfesores, name="leerProfesores"),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),

    path('estudiante/list/', EstudianteList.as_view(), name='estudiante_listar'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name='estudiante_borrar'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),

]