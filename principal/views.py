from django.shortcuts import render


def HomePage(request):
    return render(request, 'principal/home.html')

def Sobre(request):
    return render(request, 'principal/sobre.html')

def Contato(request):
    return render(request, 'principal/contato.html')

def Servicos(request):
    return render(request, 'principal/servicos.html')

def Login_Geral(request):
    return render(request, 'principal/login_geral.html')