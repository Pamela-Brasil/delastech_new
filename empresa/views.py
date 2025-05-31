from django.shortcuts import render
from .models import Empresa
from django.http import HttpResponse
from django.views import View
# Create your views here.


class Cadastro(View):
    def get(self, request):
        return HttpResponse(Empresa)