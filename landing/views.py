from django.shortcuts import render
from .forms import UsuarioForm
# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_formulario(request):
    form = UsuarioForm(request.POST)

    contexto = {
        'form': form
    }
    return render(request, 'formulario.html', contexto)

def mostrar_login(request):
    return render(request, 'login.html')