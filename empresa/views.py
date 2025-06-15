from django.shortcuts import render, redirect
from .models import Empresa
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .forms import FormEmpresa, LoginEmpresaForm

# Create your views here.

class EmpresasParceiras(ListView):
    model = Empresa
    template_name = 'empresa/emp_parceiras.html'


class Cadastro(CreateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/nova'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro Empresa Parceira'
        context['botao'] = 'Cadastrar'
        return context
    success_url = reverse_lazy('perfilemp')

   
class Edicao(UpdateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/edit.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Perfil'
        context['botao'] = 'Salvar'
        return context
    success_url = 'perfilemp'


class Exclusao(DeleteView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/deleteemp.html'
    success_url = reverse_lazy('geral_login')

def PerfilEmp(request):
    return render(request, 'empresa/perfilemp.html')

def LoginEmp(request):# View de logindef login_usuario(request):
    if request.method == 'POST':
        form = LoginEmpresaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            user = authenticate(request, username=email, password=senha)

            if user is not None:
                login(request, user)
                return redirect('perfilemp') 
            else:
                form.add_error(None, 'Email ou senha inválidos.')
    else:
        form = LoginEmpresaForm()
    
    return render(request, 'empresa/loginemp.html', {'form': form})

class LogoutEmp(View):
    #Metodo que verifica e encerra a sessão
    def get(self, request):
        if 'nome_empresa' in request.session:
            del request.session['nome_empresa']
       
        erro_message = 'Você foi desconectado! Até mais!'
        return render(request, 'empresa/loginemp.html', {'mensagem': erro_message})
        

