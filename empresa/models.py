from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Empresa(models.Model):
    PORTE_CHOICES = [
        ('PE', 'Pequena'),
        ('ME', 'Média'),
        ('GR', 'Grande'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, validators=[RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message='CNPJ deve estar no formato XX.XXX.XXX/XXXX-XX')])
    seguimento = models.CharField(max_length=20)
    porte = models.CharField(max_length=2, choices=PORTE_CHOICES)
    contato = models.EmailField(unique=True)
    

    def __str__(self):
        return f"{self.nome}"
       
    class Meta:
        verbose_name = "Empresa"
        ordering = ['nome','seguimento']
