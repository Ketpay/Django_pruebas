from django.contrib import admin

# Register your models here.
from .forms import RegistradoForm
from .models import Registrado

class adminregistrado(admin.ModelAdmin):
	list_display=['__str__','nombre','email','timestamp','actualizado']
	form=RegistradoForm
	# class Meta:
	# 	model = Registrado
admin.site.register(Registrado,adminregistrado)