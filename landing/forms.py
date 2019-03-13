from django import forms
from .models import Usuario
# Create your models here.

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('sexo',)