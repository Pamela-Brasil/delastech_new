from django import forms
from django.contrib.auth.models import User
from .models import Usuaria


class LoginUsuariaForm(forms.Form):
                  
    widgets = {
        "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
        "senha": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    }


class RegistroUsuariaForm(forms.ModelForm):
    username = forms.CharField(label='Nome de usuária')
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Usuaria
        fields = [
            'nome', 'sobrenome', 'apelido', 'cpf', 'cnpj',
            'data_nascimento', 'telefone', 'escolaridade',
            'idiomas', 'experiencia'
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu apelido'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CNPJ (opcional)'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone (opcional)'}),
            'escolaridade': forms.Select(attrs={'class': 'form-select'}),
            'idiomas': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'experiencia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva sua experiência'}),
        }
    
    def save(self, commit=True):
        # Cria o User
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha']
        )
        usuaria = super().save(commit=False)
        usuaria.user = user
        if commit:
            usuaria.save()
            self.save_m2m()  
        return usuaria
    
   
