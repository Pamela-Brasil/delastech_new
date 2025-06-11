<<<<<<< HEAD
from django import forms
from .models import Usuaria

class FormUsuaria(forms.ModelForm):
    class Meta:
        model = Usuaria 
        fields = [
            'nome'
            'sobrenome'
            'cpf'
            'cnpj'
            'data_nascimento'
            'email'
            'telefone'
            'escolaridade'
            'idiomas'
            'experiencia'
            'apelido'
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu Nome"}),
            "sobrenome": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu Sobrenome"}),
            "cpf": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu CPF"}),
            "cnpj": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu CNPJ (Opcional)"}),
            "data_nascimento": forms.DateInput(attrs={"class":"form-control","placeholder":"DD/MM/AAAA", 'type':'date'}),
            "email": forms.EmailInput(attrs={"class":"form-control","placeholder":"email@example.com"}),
            "telefone": forms.TextInput(attrs={"class":"form-control","placeholder":"(XX)XXXXX-XXXX"}),
            "escolaridade": forms.TextInput(attrs={"class":"form-control","placeholder":"Liste sua Formação"}),
            "idiomas": forms.CheckboxSelectMultiple(attrs={"class":"form-control","placeholder":"Selecione os idiomas que domina"}),
            "experiencia": forms.TextInput(attrs={"class":"form-control","placeholder":"Nos conte as suas experiencias profissionais"}),
            "apelido": forms.TextInput(attrs={"class":"form-control","placeholder":"Como quer que a gente te chame?"})
=======
from django import forms
from .models import Usuaria

class FormUsuaria(forms.ModelForm):
    class Meta:
        model = Usuaria 
        fields = [
            'nome'
            'sobrenome'
            'cpf'
            'cnpj'
            'data_nascimento'
            'email'
            'telefone'
            'escolaridade'
            'idiomas'
            'experiencia'
            'apelido'
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu Nome"}),
            "sobrenome": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu Sobrenome"}),
            "cpf": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu CPF"}),
            "cnpj": forms.TextInput(attrs={"class":"form-control","placeholder":"Digite seu CNPJ (Opcional)"}),
            "data_nascimento": forms.DateInput(attrs={"class":"form-control","placeholder":"DD/MM/AAAA", 'type':'date'}),
            "email": forms.EmailInput(attrs={"class":"form-control","placeholder":"email@example.com"}),
            "telefone": forms.TextInput(attrs={"class":"form-control","placeholder":"(XX)XXXXX-XXXX"}),
            "escolaridade": forms.TextInput(attrs={"class":"form-control","placeholder":"Liste sua Formação"}),
            "idiomas": forms.CheckboxSelectMultiple(attrs={"class":"form-control","placeholder":"Selecione os idiomas que domina"}),
            "experiencia": forms.TextInput(attrs={"class":"form-control","placeholder":"Nos conte as suas experiencias profissionais"}),
            "apelido": forms.TextInput(attrs={"class":"form-control","placeholder":"Como quer que a gente te chame?"})
>>>>>>> d79063c23d590f9d216d02ec4f01b8bb8d811ea2
        }