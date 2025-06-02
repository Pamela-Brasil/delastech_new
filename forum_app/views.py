from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def forum_home(request):
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'forum_app/forum_home.html', {'postagens': posts})

@login_required
def novo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('forum_home')
    else:
        form = PostForm()
    return render(request, 'forum_app/novo_post.html', {'form': form})