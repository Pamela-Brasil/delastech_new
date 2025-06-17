from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import reverse_lazy, reverse
from .models import Usuaria
from django.contrib.auth import authenticate, login, logout
from .forms import LoginUsuariaForm, RegistroUsuariaForm as FormUsuaria
from django.views.generic import ListView,CreateView,UpdateView, DeleteView, View
from django.conf import settings
from django.contrib.auth.models import User

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
        context['pagina'] = 'Cadastro Delas | DelasTech'
        context['titulo'] = 'Cadastro Delas'
        context['botao'] = 'Cadastrar'
        return context
  
    

class EdicaoUs(UpdateView):
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/novausuaria.html'
    success_url = reverse_lazy('usuaria/perfiluser.html') 

    pk_url_kwarg = 'id'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagina'] = 'Editar Cadastro | DelasTech'
        context['titulo'] = 'Editar Perfil'
        context['botao'] = 'Salvar'
        return context
    def get_success_url(self):
        return reverse('perfil_user')
    
    
class ListaUsuarias(ListView):  #Nessa class, mais tarde entrará a página de consulta das empresas com filtro
    model = Usuaria
    form_class = FormUsuaria
    template_name = 'usuaria/candidatas.html'



def Exclusao(request, id):
    usuaria = get_object_or_404(Usuaria, id=id)

    if request.method == 'POST':
        user = usuaria.user  # pega o usuário relacionado
        usuaria.delete()
        user.delete()
        return redirect('home')
    return render(request, 'usuaria/deleteuser.html', {'usuaria': usuaria})


def Perfil(request):
    usuaria_id = request.session.get('usuaria_id')
    if not usuaria_id:
        return redirect('geral_login')  # ou algum tratamento

    usuaria = get_object_or_404(Usuaria, id=usuaria_id)
    return render(request, 'usuaria/perfiluser.html', {'usuaria': usuaria})


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
                    form.add_error(None, 'Desculpe, essa usuária não existe!') # Lidar com o caso de um User existir mas não ter um perfil Usuaria associado
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
    return redirect('home')
   