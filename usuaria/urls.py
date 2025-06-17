from django.urls import path
from .views import CadastroUs, EdicaoUs,ListaUsuarias, Exclusao, Perfil, Logout, LoginUser


urlpatterns = [
    path('novadela/', CadastroUs.as_view(), name="nova_user"),
    path('editarela/<int:id>/', EdicaoUs.as_view(), name="edit_user"),
    path('candidatas/', ListaUsuarias.as_view(), name="candidatas"),
    path('deleta/<int:id>/', Exclusao, name="delete_user"),
    path('logindela/', LoginUser ,name="login_user"),
    path('perfildela/', Perfil, name="perfil_user"),
    path('logoutdela/', Logout, name="logout_user"),
]
