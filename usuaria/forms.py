from django import forms
from django.contrib.auth.models import User
from .models import Usuaria, Idioma


class LoginUsuariaForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}))
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))


class RegistroUsuariaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))
    confirmacao_senha = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}))
    idiomas = forms.ModelMultipleChoiceField(queryset=Idioma.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),required=False,label="Idiomas que você domina")
    

    class Meta:
        model = Usuaria
        fields = [
            'nome', 'sobrenome', 'apelido', 'cpf', 'cnpj',
            'telefone', 'escolaridade',
            'idiomas', 'experiencia', 'email','data_nascimento'
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu apelido'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CNPJ (opcional)'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu telefone (opcional)'}),
            'escolaridade': forms.Select(attrs={'class': 'form-select'}),
            'experiencia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva sua experiência'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}, format='%d/%m/%Y'),
        }

    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está cadastrado. Por favor, use outro.")
        return email
    
    def save(self, commit=True):
        # Cria o User
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha']
        )
        usuaria = super().save(commit=False)
        usuaria.user = user
        usuaria.senha = self.cleaned_data.get('senha') 
        if commit:
            usuaria.save()
            self.save_m2m()  
        return usuaria
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha and senha != confirmacao_senha:
            self.add_error('confirmacao_senha', "As senhas não coincidem.")
    
