from django.shortcuts import render
from landing.forms import CadastroForm
# Create your views here.

def mostrar_index(request):
    return render(request, 'index2.html')

def mostrar_formulario(request):
    formulario = CadastroForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm()

    context = {
        'form': formulario
    }

    return render(request, 'formulario.html', context)

def mostrar_login(request):
    return render(request, 'login2.html')

def mostrar_conta(request):
    return render(request, 'conta.html')