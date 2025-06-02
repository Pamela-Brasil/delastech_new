from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home.html'),
    path('novo/', views.novo_post, name='criar_postagem.html'),
]
