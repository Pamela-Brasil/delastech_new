from django.urls import path
from .views import EmpresasParceiras, Cadastro, Edicao, Exclusao, PerfilEmp, LoginEmp, Logout   

urlpatterns = [
    path('parceiras/', EmpresasParceiras.as_view(), name="empresasparceiras"),
    path('cadastro/', Cadastro.as_view(), name="novaparceira"),
    path('editarempresa/<int:id>/', Edicao.as_view(), name="editarempresa"),
    path('deletemp/<int:id>/', Exclusao, name="delete_emp"),
    path('perfilemp/', PerfilEmp, name="perfilemp"),
    path('loginempresa/', LoginEmp, name="login_emp"),
    path('logoutempresa/', Logout, name="logout_emp"),

]
