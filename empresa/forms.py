from django import forms
from django.contrib.auth.models import User
from .models import Empresa


class LoginEmpresaForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}))
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))


class FormEmpresa(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))
    confirmacao_senha = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}))
    
    class Meta:
        model = Empresa
        fields = [
            'nome',
            'cnpj',
            'seguimento',
            'porte',
            'email',
        ]
    
       
        widgets = {
                'nome':forms.TextInput(attrs={"class":"form-control","placeholder":"Nome da Empresa"}),
                'cnpj': forms.TextInput(attrs={"class":"form-control","placeholder":"Digite o CNPJ"}),
                'seguimento': forms.TextInput(attrs={"class":"form-control","placeholder":"Seguimento de Mercado"}),
                'porte': forms.Select(attrs={"class":"form-control","placeholder":"Porte da Empresa"}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'})
            }
        

    def save(self, commit=True):
        empresa = super().save(commit=False)

        if not empresa.user_id:
            user = User.objects.create_user(
                username=self.cleaned_data['email'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['senha']
            )
            empresa.user = user
        else:
            user = empresa.user
            user.username = self.cleaned_data['email']
            user.email = self.cleaned_data['email']
            if self.cleaned_data.get('senha'):
                user.set_password(self.cleaned_data['senha'])
            user.save()

        if commit:
            empresa.save()

        return empresa

        
    def clean_email(self):
        email = self.cleaned_data['email']
        user_qs = User.objects.filter(username=email)

        if self.instance.user_id:
            user_qs = user_qs.exclude(pk=self.instance.user.pk)

        if user_qs.exists():
            raise forms.ValidationError("Este e-mail já está em uso.")

        return email

 

    
    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmacao_senha = cleaned_data.get("confirmacao_senha")

        if senha and confirmacao_senha and senha != confirmacao_senha:
            self.add_error('confirmacao_senha', "As senhas não coincidem.")



