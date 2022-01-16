from http.client import HTTPResponse
from django.shortcuts import render

from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def  crear_curso(self, nombre, camada):

    curso= Curso(nombre=nombre, camada=camada)
    
    curso.save() ###Guardar para que se refleje en la base de datos###

    return HttpResponse(f'Se creo el curso de {curso.nombre} con el numero de camada: {curso.camada}') 
