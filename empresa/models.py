from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    seguimento = models.CharField(max_length=20)
    porte = models.CharField(max_length=7)
    contato = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} {self.seguimento}"
    
    class Meta:
        verbose_name = "Empresa"
        ordering = ['nome','seguimento']

