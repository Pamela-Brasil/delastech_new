from django.urls import path
from .views import (
    forum_home,
    login_view,
    logout_view,
    novo_post,
    editar_post,
    excluir_post,
)

urlpatterns = [
    path('', forum_home, name='forum_home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('criar/', novo_post, name='criar_postagem'),
    path('editar/<int:post_id>/', editar_post, name='editar_postagem'),  
    path('excluir/<int:post_id>/', excluir_post, name='excluir_postagem'),  
]
