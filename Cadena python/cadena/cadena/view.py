#--------------Lbrerias--------------
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render
import os 
#--------------Variables--------------


#--------------Funciones--------------


def Index(request):	#primera cara
	doc_externo=open("C:/Users/Samuel/Desktop/Cadena python/cadena/cadena/HTML/Index.html")
	plt=Template(doc_externo.read())
	doc_externo.close
	ctx=Context() 
	Doc=plt.render(ctx)
	return HttpResponse (Doc)


def formulario(request):	#formulario
	return render(request,"formulario.html          ")

def proceso(request):	#Recepcion de datos
	nombre=request.GET["nombre"]
	apellido=request.GET["apellido"]
	email=request.GET["email"]
	sexo=request.GET["sexo"]
	archivo=request.GET["archivo"]
	doc_externo=open("C:/Users/Samuel/Desktop/Cadena python/cadena/cadena/HTML/proceso.html")
	plt=Template(doc_externo.read())
	doc_externo.close
	ctx=Context({"nombre":nombre, "apellido":apellido , "email":email , "sexo":sexo, "archivo":archivo }) #puede recibir diccionarios
	Doc=plt.render(ctx)
	return HttpResponse (Doc)
