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
<<<<<<< HEAD
    success_urls = ''
=======
    success_urls = 
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2


class EdicaoUs(UpdateView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/edituser.html'
<<<<<<< HEAD
    success_url = ''
=======
    success_url = 
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2
  

class ListaUsuarias(ListView):  #Nessa class, mais tarde entrará a página de consulta das empresas com filtro
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/candidatas.html'
    

class Exclusao(DeleteView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/delete'
<<<<<<< HEAD
    success_url = ''
=======
    success_url = ''
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2
