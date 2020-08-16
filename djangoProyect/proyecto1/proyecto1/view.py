from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):	#primera vista
	nombre="Samuel"
	apellido="garcia"
	ahora=datetime.datetime.now()
	doc_externo=open("C:/Users/Samuel/Desktop/djangoProyect/proyecto1/proyecto1/Plantillas/miplantilla.html")
	plt=Template(doc_externo.read())
	doc_externo.close
	ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido , "time":ahora }) #puede recibir diccionarios
	Doc=plt.render(ctx)
	return HttpResponse (Doc)
def salida(request):	#2da vista

	return HttpResponse ("byebye Jotos")
def fecha(request):	#fecha
	fecha_actual=datetime.datetime.now()
	fehca_formato="""<html><body><h1>
	Fecha Actual %s
	</h1></body></html>""" %fecha_actual
	return HttpResponse (fehca_formato)
def boton (request):
	doc_externo=open("C:/Users/Samuel/Desktop/djangoProyect/proyecto1/proyecto1/Plantillas/botones.html")
	plt=Template(doc_externo.read())
	doc_externo.close
	ctx=Context() #puede recibir diccionarios
	Doc=plt.render(ctx)
	return HttpResponse (Doc)