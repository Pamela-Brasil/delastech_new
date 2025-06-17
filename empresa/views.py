from django.shortcuts import render, redirect,get_object_or_404
from .models import Empresa
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from .forms import FormEmpresa, LoginEmpresaForm
from django.conf import settings

# Create your views here.

class EmpresasParceiras(ListView):
    model = Empresa
    template_name = 'empresa/emp_parceiras.html'


class Cadastro(CreateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/nova.html'
    def form_valid(self, form):
        empresa = form.save()
        self.request.session['empresa_id'] = empresa.id  
        login(self.request, empresa.user) 
        return redirect('empresa/perfilemp.html')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagina'] = 'Cadastro Empresa Parceira | DelasTech'
        context['titulo'] = 'Cadastro Empresa Parceira'
        context['botao'] = 'Cadastrar'
        return context


   
class Edicao(UpdateView):
    model = Empresa
    form_class = FormEmpresa
    template_name = 'empresa/nova.html'
    success_url = reverse_lazy('perfilemp') 

    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagina'] = 'Editar Cadastro | DelasTech'
        context['titulo'] = 'Editar Perfil'
        context['botao'] = 'Salvar'
        return context
    def get_success_url(self):
        return reverse('perfilemp')


def Exclusao(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method == 'POST':
        user = empresa.user  
        empresa.delete()
        user.delete()
        return redirect('home')
    return render(request, 'empresa/deleteemp.html', {'empresa': empresa})

def PerfilEmp(request):
    empresa_id = request.session.get('empresa_id')
    if not empresa_id:
        return redirect('geral_login')  # ou algum tratamento

    empresa = get_object_or_404(Empresa, id=empresa_id)
    return render(request, 'empresa/perfilemp.html', {'empresa': empresa})

def LoginEmp(request):# View de logindef login_usuario(request):
    print(f"DEBUG: LANGUAGE_CODE atual: {settings.LANGUAGE_CODE}") 
    
    if request.method == 'POST':
        form = LoginEmpresaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            user = authenticate(request, username=email, password=senha)

            if user is not None:
                login(request, user)
                try:
                    empresa = Empresa.objects.get(user=user)
                    request.session['empresa_id'] = empresa.id
                except Empresa.DoesNotExist:
                    form.add_error(None, 'Desculpe, esse usuário não existe!')# Lidar com o caso de um User existir mas não ter um perfil Usuaria associado
                    pass # Ou redirecionar para

                return redirect('perfilemp') 
            else:
                form.add_error(None, 'Email ou senha inválidos.')
    else:
        form = LoginEmpresaForm()
    
    return render(request, 'empresa/loginemp.html', {'form': form})

def Logout(request): 
    if request.user.is_authenticated: 
        logout(request) 
        
        if 'empresa_id' in request.session:
            del request.session['empresa_id']
    return redirect('home')  