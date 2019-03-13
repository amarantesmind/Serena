from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_formulario(request):
    return render(request, 'formulario.html')

def mostrar_login(request):
    return render(request, 'login.html')