# Generated by Django 2.1.7 on 2019-03-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.PositiveIntegerField(max_length=11)),
                ('cep', models.PositiveIntegerField(max_length=8)),
                ('numero', models.PositiveIntegerField(max_length=6)),
                ('nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('FEM', 'Feminino'), ('MASC', 'Masculino'), ('NB', 'Não binário')], default='FEM', max_length=2)),
                ('profissao', models.CharField(max_length=40)),
                ('nome_emergencia1', models.CharField(max_length=30)),
                ('email_emergencia1', models.EmailField(max_length=254)),
                ('tel_emergencia1', models.PositiveIntegerField(max_length=11)),
                ('nome_emergencia2', models.CharField(max_length=30)),
                ('email_emergencia2', models.EmailField(max_length=254)),
                ('tel_emergencia2', models.PositiveIntegerField(max_length=11)),
            ],
        ),
    ]
