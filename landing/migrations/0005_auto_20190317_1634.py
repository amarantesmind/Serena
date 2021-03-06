# Generated by Django 2.1.7 on 2019-03-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20190317_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='celular',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='cep',
            field=models.PositiveIntegerField(verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='nascimento',
            field=models.DateTimeField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='sexo',
            field=models.CharField(choices=[('FEM', 'Feminino'), ('MASC', 'Masculino'), ('NB', 'Não binário')], default='FEM', max_length=3, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='tel_emergencia1',
            field=models.PositiveIntegerField(verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='tel_emergencia2',
            field=models.PositiveIntegerField(verbose_name='Telefone'),
        ),
    ]
