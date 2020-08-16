from django.contrib import admin

# Register your models here.
from .forms import RegForm
from .models import Registrado

class adminregistrado(admin.ModelAdmin):
	list_display=['__str__','nombre','edad','media']
	form=RegForm
	# class Meta:
	# 	model = Registrado
admin.site.register(Registrado,adminregistrado)