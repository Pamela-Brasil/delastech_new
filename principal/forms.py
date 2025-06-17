from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xx) xxxxx-xxxx'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto da mensagem'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 4}),
        }
