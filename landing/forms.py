from django import forms
from landing.models import Cadastro
# Create your models here.

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        widgets = {
            'senha': forms.PasswordInput(),
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
            'nome_emergencia1',
            'email_emergencia1',
            'tel_emergencia1',
            'nome_emergencia2',
            'email_emergencia2',
            'tel_emergencia2',
        ]
