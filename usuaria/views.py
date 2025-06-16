from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Usuaria
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUsuariaForm, RegistroUsuariaForm as FormUsuaria
from django.views.generic import ListView,CreateView,UpdateView, DeleteView, View
from django.conf import settings

# Create your views here.
class CadastroUs(CreateView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/novausuaria.html'
    def form_valid(self, form):
        usuaria = form.save()
        self.request.session['usuaria_id'] = usuaria.id  
        login(self.request, usuaria.user) 
        return redirect('perfil_user') 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro Delas'
        context['botao'] = 'Cadastrar'
        return context
  
    

class EdicaoUs(UpdateView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/novausuaria.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Perfil'
        context['botao'] = 'Salvar'
        return context
    success_url = 'usuaria/perfiluser.html' 
  

class ListaUsuarias(ListView):  #Nessa class, mais tarde entrará a página de consulta das empresas com filtro
    model = Usuaria
    form_class = FormUsuaria

    def get(self, request, *args, **kwargs):

        #Verificar se a sessão tem 'nome_cliente'
        if 'nome_empresa' not in request.session:
            return redirect('login_empresa') #retorna para o formulario
        
        #Se a sessao existir e o usaurio esriver autenticado segue enfrente
        return super().get(request, *args, **kwargs)
    
    template_name = 'usuaria/candidatas.html'

class Exclusao(DeleteView):
    model = Usuaria
    template_name = 'usuaria/deleteuser.html'
    success_url = reverse_lazy('geral_login')

def Perfil(request):
    if request.user.is_authenticated:
        try:
            usuaria = Usuaria.objects.get(user=request.user)
            return render(request, 'usuaria/perfiluser.html', {'usuaria': usuaria})
        except Usuaria.DoesNotExist:
            # Se o Usuaria perfil não existe para o User logado (erro na criação ou inconsistência)
            # Você pode redirecionar para uma página de erro ou criar o perfil Usuaria
            return redirect('cadastro_incompleto_ou_erro') # Crie esta URL/view
    return redirect('login') # Redireciona para o login se não estiver autenticado
  

def LoginUser(request):
    print(f"DEBUG: LANGUAGE_CODE atual: {settings.LANGUAGE_CODE}") 

    if request.method == 'POST':
        form = LoginUsuariaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            user = authenticate(request, username=email, password=senha)

            if user is not None:
                login(request, user)
                try:
                    usuaria = Usuaria.objects.get(user=user)
                    request.session['usuaria_id'] = usuaria.id
                except Usuaria.DoesNotExist:
                    # Lidar com o caso de um User existir mas não ter um perfil Usuaria associado
                    pass # Ou redirecionar para um "complete seu perfil"

                return redirect('perfil_user')
            else:
                form.add_error(None, 'Email ou senha inválidos. Por favor, tente novamente.')
    else:
        form = LoginUsuariaForm()
    
    return render(request, 'usuaria/loginuser.html', {'form': form})


def Logout(request): 
    if request.user.is_authenticated: 
        logout(request) 
        
        if 'usuaria_id' in request.session:
            del request.session['usuaria_id']
    return redirect('geral_login')
   