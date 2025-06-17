from django.shortcuts import render, redirect
from .forms import ContatoForm
from django.contrib import messages

def Contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso! 💌')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'principal/contato.html', {'form': form})


def HomePage(request):
    return render(request, 'principal/home.html')

def Sobre(request):
    return render(request, 'principal/sobre.html')

def Servicos(request):
    return render(request, 'principal/servicos.html')

def Login_Geral(request):
    return render(request, 'principal/login_geral.html')