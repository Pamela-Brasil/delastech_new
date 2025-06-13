from django.urls import path
from .views import HomePage, Sobre, Contato, Servicos

urlpatterns = [
    path('', HomePage, name='home'),
    path('sobre/', Sobre, name='sobre'),
    path('contato/', Contato, name='contato'),
    path('servicos/', Servicos, name='servicos'),
]