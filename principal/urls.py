from django.urls import path
from .views import HomePage, Sobre, Contato, Servicos, Login_Geral

urlpatterns = [
    path('', HomePage, name='home'),
    path('sobre/', Sobre, name='sobre'),
    path('contato/', Contato, name='contato'),
    path('servicos/', Servicos, name='servicos'),
    path('logingen/', Login_Geral, name='geral_login'),
]