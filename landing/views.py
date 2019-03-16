from django.shortcuts import render
# Create your views here.

def mostrar_index(request):
    return render(request, 'index2.html')

def mostrar_formulario(request):
    return render(request, 'formulario.html', contexto)

def mostrar_login(request):
    return render(request, 'login2.html')