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

    username = models.CharField(max_length=30)
    senha = models.CharField(max_length=15)
    nome = models.CharField(max_length=40)
    email = models.EmailField(verbose_name="E-mail")
    celular = models.PositiveIntegerField(max_length=11)
    cep = models.PositiveIntegerField(max_length=8, verbose_name="CEP")
    numero = models.PositiveIntegerField(max_length=6, verbose_name="Número")
    nascimento = models.DateField()
    sexo = models.CharField(max_length=2, verbose_name="Gênero", choices=GENERO, default=FEMININO)
    profissao = models.CharField(max_length=40, verbose_name="Profissão")
    nome_emergencia1 = models.CharField(max_length=30, verbose_name="Nome")
    email_emergencia1 = models.EmailField(verbose_name="E-mail")
    tel_emergencia1 = models.PositiveIntegerField(max_length=11, verbose_name="Telefone")
    nome_emergencia2 = models.CharField(max_length=30, verbose_name="Nome")
    email_emergencia2 = models.EmailField(verbose_name="E-mail")
    tel_emergencia2 = models.PositiveIntegerField(max_length=11, verbose_name="Telefone")

    def __str__(self):
        return self.username