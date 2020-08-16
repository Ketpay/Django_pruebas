from django import forms
from .models import Registrado

class RegForm(forms.ModelForm):
	class Meta:
		model= Registrado
		fields=["nombre","email","edad","media"]

	def __str__(self):
		return self.email
