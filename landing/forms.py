from django import forms
from landing.models import Cadastro
# Create your models here.

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        widgets = {
            'senha': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'cep': forms.DateTimeInput(),
            'nascimento': forms.DateTimeInput(),
            'tel_emergencia1': forms.DateInput(),
        }
        fields = [
            'username',
            'senha',
            'nome',
            'email',
            'celular',
            'cep',
            'nascimento',
            'sexo',
            'profissao',
            'grau_parentesco',
            'nome_emergencia1',
            'email_emergencia1',
            'tel_emergencia1',
        ]
