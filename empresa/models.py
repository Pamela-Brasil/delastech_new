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
    cnpj = models.CharField(max_length=18, unique=True)
    seguimento = models.CharField(max_length=20)
    porte = models.CharField(max_length=2, choices=PORTE_CHOICES)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return f"{self.nome}"
       
    class Meta:
        verbose_name = "Empresa"
        ordering = ['nome','seguimento']
