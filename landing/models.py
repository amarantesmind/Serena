from django.db import models
# from . import forms

# Create your models here.

class Cadastro(models.Model):
    FEMININO = 'FEM'
    MASCULINO = 'MASC'
    NAO_BINARIO = 'NB'

    GENERO = [
        (FEMININO, 'Feminino'),
        (MASCULINO, 'Masculino'),
        (NAO_BINARIO, 'Não binário')
    ]

    username = models.CharField(max_length=30, verbose_name="User")
    senha = models.CharField(max_length=15)
    nome = models.CharField(max_length=40)
    email = models.EmailField(verbose_name="E-mail")
    celular = models.CharField(max_length=11)
    cep = models.CharField(max_length=8, verbose_name="CEP")
    nascimento = models.DateTimeField(max_length=8)
    sexo = models.CharField(max_length=3, verbose_name="Gênero", choices=GENERO, default=FEMININO)
    profissao = models.CharField(max_length=40, verbose_name="Profissão")
    grau_parentesco = models.CharField(max_length=10, default='')
    nome_emergencia1 = models.CharField(max_length=30, verbose_name="Nome")
    email_emergencia1 = models.EmailField(verbose_name="E-mail")
    tel_emergencia1 = models.PositiveIntegerField(verbose_name="Telefone")

    def __str__(self):
        return self.username

    