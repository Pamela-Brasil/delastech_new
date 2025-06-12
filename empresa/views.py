from django.shortcuts import render, redirect
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
    success_url = reverse_lazy('empresa:empresas-parceiras')

class Edicao(UpdateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/edit'
    success_url = ''


class Exclusao(DeleteView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/delete'
    success_url = ''
