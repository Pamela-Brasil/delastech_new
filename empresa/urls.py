from django.urls import path
from .views import EmpresasParceiras, Cadastro, Edicao

urlpatterns = [
    path('parceiras/', EmpresasParceiras.as_view(), name="empresas_parceiras"),
    path('cadastro/', Cadastro.as_view(), name="nova_parceira"),
    path('editarempresa/', Edicao.as_view(), name="editar_empesa"),
    path('deletemp/', Exclusao.as_view(), name="delete_emp"),
]
