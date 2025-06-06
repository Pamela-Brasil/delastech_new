from django.urls import path

urlpatterns = [
    path('novadela/', CadastroUs.as_view(), name="nova_user"),
    path('editarela/', EdicaoUs.as_view(), name="edit_user"),
    path('candidatas/', ListaUsuarias.as_view(), name="candidatas"),
]
