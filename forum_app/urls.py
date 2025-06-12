from django.urls import path
from .views import forum_home, login_view, logout_view, novo_post

urlpatterns = [
    path('', forum_home, name='forum_home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('criar/', novo_post, name='criar_postagem'),
]
