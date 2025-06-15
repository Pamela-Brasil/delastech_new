from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Usuaria
from django.contrib.auth import authenticate, login
from .forms import LoginUsuariaForm, RegistroUsuariaForm as FormUsuaria
from django.views.generic import ListView,CreateView,UpdateView, DeleteView, View

# Create your views here.
class CadastroUs(CreateView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/novausuaria.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro Delas'
        context['botao'] = 'Cadastrar'
        return context
    success_url = reverse_lazy('perfil_user')
    

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
    form_class = FormUsuaria
    template_name = 'usuaria/deleteuser.html'
    success_url = reverse_lazy('geral_login')

def Perfil(request):
    return render(request, 'usuaria/perfiluser.html')

def LoginUser(request):
    if request.method == 'POST':
        form = LoginUsuariaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            user = authenticate(request, username=email, password=senha)

            if user is not None:
                login(request, user)
                return redirect('perfil_user') 
            else:
                form.add_error(None, 'Email ou senha inválidos.')
    else:
        form = LoginUsuariaForm()
    
    return render(request, 'usuaria/loginuser.html', {'form': form})

# View de logout
class Logout(View):
    #Metodo que verifica e encerra a sessão
    def get(self, request):
        if 'nome_usuaria' in request.session:
            del request.session['nome_usuaria']
       
        erro_message = 'Você foi desconectada! Até mais!'
        return render(request, 'usuaria/loginuser.html', {'mensagem': erro_message})
        

