from django.urls import path
from .views import forum_home, novo_post

urlpatterns = [
    path('', forum_home, name='forum_home'),
    path('novo/', novo_post, name='criar_postagem'),
]
