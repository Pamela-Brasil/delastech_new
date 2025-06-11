from django.shortcuts import render
from .models import Empresa
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormEmpresa

# Create your views here.


class EmpresasParceiras(ListView):
    model = Empresa
    template_name = 'empresa/emp-parceiras.html'

class Cadastro(CreateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/nova'
<<<<<<< HEAD
    success_url = ''
=======
    success_url = 
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2

class Edicao(UpdateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/edit'
<<<<<<< HEAD
    success_url = ''
=======
    success_url = 
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2


class Exclusao(DeleteView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/delete'
<<<<<<< HEAD
    success_url = ''
=======
    success_url = ''
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2
