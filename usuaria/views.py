from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuaria
from .forms import FormUsuaria
from django.views.generic import ListView,CreateView,UpdateView, DeleteView

# Create your views here.
class CadastroUs(CreateView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/novausuaria.html'
    success_urls = ''


class EdicaoUs(UpdateView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/edituser.html'
    success_url = ''
  

class ListaUsuarias(ListView):  #Nessa class, mais tarde entrará a página de consulta das empresas com filtro
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/candidatas.html'
    

class Exclusao(DeleteView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/delete'
    success_url = ''

# Página principal do fórum 
@login_required(login_url='login')
def forum_home(request):
    return render(request, 'forum_home.html')  

# View de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum_home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

# View de logout
def logout_view(request):
    logout(request)
    return redirect('login')
