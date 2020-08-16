from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model=Registrado
		fields=['nombre','email']
	def clean_email(self):
		email=self.cleaned_data.get('email')
		# if not "edu" in email:
		# 	raise forms.ValidationError("porfavor utilice un email con la extencion .edu")

		print(email)
		return email

class RegForm(forms.Form):
	nombre=forms.CharField(max_length=100)
	edad=forms.IntegerField()

