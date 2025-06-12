from django.urls import path
from .views import CadastroUs, EdicaoUs,ListaUsuarias, Exclusao


urlpatterns = [
    path('novadela/', CadastroUs.as_view(), name="nova_user"),
    path('editarela/', EdicaoUs.as_view(), name="edit_user"),
    path('candidatas/', ListaUsuarias.as_view(), name="candidatas"),
    path('deleta/', Exclusao.as_view(), name="delete_user"),
]
