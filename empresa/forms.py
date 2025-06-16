from django import forms
from django.contrib.auth.models import User
from .models import Empresa

class FormEmpresa(forms.ModelForm):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}))
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Empresa
        fields = [
            'nome',
            'cnpj',
            'seguimento',
            'porte',
            'contato',
        ]
    
       
    widgets = {
            "nome":forms.TextInput(attrs={"class":"form-control","placeholder":"Nome da Empresa"}),
            "cnpj": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite o CNPJ"}),
            "seguimento": forms.TextInput(attrs={"class":"form-control","placeholder":"Seguimento de Mercado"}),
            "porte": forms.TextInput(attrs={"class":"form-control","placeholder":"Porte da Empresa"}),
            "contato": forms.EmailInput(attrs={"class":"form-control","placeholder":"E-mail de Contato"}),
        }
    
    def clean_username(self):
        username = self.cleaned_data['nome']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso. Por favor, escolha outro.")
        return username

   
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está cadastrado. Por favor, use outro.")
        return email

    def save(self, commit=True):
        # Cria o User
        user = User.objects.create_user(
            username=self.cleaned_data['nome'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha']
        )
        empresa = super().save(commit=False)
        empresa.user = user
        empresa.senha = self.cleaned_data.get('senha') 
        if commit:
            empresa.save()
            self.save_m2m()  
        return empresa

class LoginEmpresaForm(forms.Form):
    widgets = {
        "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
        "senha": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    }