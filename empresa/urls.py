<<<<<<< HEAD

from django.urls import path
from .views import EmpresasParceiras, Cadastro, Edicao, Exclusao

urlpatterns = [
    path('parceiras/', EmpresasParceiras.as_view(), name="empresas_parceiras"),
    path('cadastro/', Cadastro.as_view(), name="nova_parceira"),
    path('editarempresa/', Edicao.as_view(), name="editar_empesa"),
    path('deletemp/', Exclusao.as_view(), name="delete_emp"),
]
=======
from django.urls import path
from .views import EmpresasParceiras, Cadastro, Edicao, Exclusao

urlpatterns = [
    path('parceiras/', EmpresasParceiras.as_view(), name="empresas_parceiras"),
    path('cadastro/', Cadastro.as_view(), name="nova_parceira"),
    path('editarempresa/', Edicao.as_view(), name="editar_empesa"),
    path('deletemp/', Exclusao.as_view(), name="delete_emp"),
]
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2
