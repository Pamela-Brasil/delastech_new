from django import forms
from django.contrib.auth.models import User
from .models import Empresa

class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nome',
            'cnpj',
            'seguimento',
            'porte',
            'contato',
            'senha',
        ]
    
    def save(self, commit=True):
        # Cria o User
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha']
        )
        empresa = super().save(commit=False)
        empresa.user = user
        if commit:
            empresa.save()
            self.save_m2m()  
        return empresa
       
    widgets = {
            "nome":forms.TextInput(attrs={"class":"form-control","placeholder":"Nome da Empresa"}),
            "cnpj": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite o CNPJ"}),
            "seguimento": forms.TextInput(attrs={"class":"form-control","placeholder":"Seguimento de Mercado"}),
            "porte": forms.TextInput(attrs={"class":"form-control","placeholder":"Porte da Empresa"}),
            "contato": forms.EmailInput(attrs={"class":"form-control","placeholder":"E-mail de Contato"}),
            "senha": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
        }

class LoginEmpresaForm(forms.Form):
    widgets = {
        "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
        "senha": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    }