from django.urls import path
from .views import EmpresasParceiras, Cadastro, Edicao, Exclusao, PerfilEmp, LoginEmp, LogoutEmp    

urlpatterns = [
    path('parceiras/', EmpresasParceiras.as_view(), name="empresasparceiras"),
    path('cadastro/', Cadastro.as_view(), name="novaparceira"),
    path('editarempresa/', Edicao.as_view(), name="editarempesa"),
    path('deletemp/', Exclusao.as_view(), name="delete_emp"),
    path('perfilemp/', PerfilEmp, name="perfilemp"),
    path('loginempresa/', LoginEmp, name="login_emp"),
    path('logoutempresa/', LogoutEmp.as_view(), name="logout_emp"),

]
