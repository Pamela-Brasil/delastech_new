from django.shortcuts import render
from .models import Usuaria
from .forms import FormUsuaria
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

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
