from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post

# Página principal do fórum 
@login_required(login_url='login')
def forum_home(request):
    postagens = Post.objects.all().order_by('-criado_em')
    return render(request, 'forum_app/forum_home.html', {'postagens': postagens})

# Página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum_home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'forum_app/login.html')

# Logout do sistema
def logout_view(request):
    logout(request)
    return redirect('login')

# Criar nova postagem
@login_required(login_url='login')
def novo_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        if titulo and conteudo:
            Post.objects.create(autor=request.user, titulo=titulo, conteudo=conteudo)
            return redirect('forum_home')
        else:
            messages.error(request, 'Preencha todos os campos.')
    return render(request, 'forum_app/criar_postagem.html')