<<<<<<< HEAD
from django import forms
from .models import Empresa

class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nome'
            'cnpj'
            'seguimento'
            'porte'
            'contato'
        ]
        widgets = {
            "nome":forms.TextInput(attrs={"class":"form-control","placeholder":"Nome da Empresa"}),
            "cnpj": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite o CNPJ"}),
            "seguimento": forms.TextInput(attrs={"class":"form-control","placeholder":"Seguimento de Mercado"}),
            "porte": forms.TextInput(attrs={"class":"form-control","placeholder":"Porte da Empresa"}),
            "contato": forms.EmailInput(attrs={"class":"form-control","placeholder":"E-mail de Contato"})
        }
=======
from django import forms
from .models import Empresa

class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nome'
            'cnpj'
            'seguimento'
            'porte'
            'contato'
        ]
        widgets = {
            "nome":forms.TextInput(attrs={"class":"form-control","placeholder":"Nome da Empresa"}),
            "cnpj": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite o CNPJ"}),
            "seguimento": forms.TextInput(attrs={"class":"form-control","placeholder":"Seguimento de Mercado"}),
            "porte": forms.TextInput(attrs={"class":"form-control","placeholder":"Porte da Empresa"}),
            "contato": forms.EmailInput(attrs={"class":"form-control","placeholder":"E-mail de Contato"})
        }
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2
