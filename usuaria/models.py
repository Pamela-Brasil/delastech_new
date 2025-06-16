from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Idioma(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
    

class Usuaria(models.Model):
    ESCOLARIDADE_CHOICES = [
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Ensino Superior'),
        ('pos', 'Pós-Graduação'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    cnpj = models.CharField(max_length=14, unique=True, blank=True, null=True)
    data_nascimento = models.DateField()
    email =  models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    escolaridade = models.CharField(max_length=30,choices=ESCOLARIDADE_CHOICES)
    idiomas = models.ManyToManyField(Idioma)
    experiencia = models.TextField()
    apelido = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return f"{self.apelido}" or f"{self.nome} {self.sobrenome}"
    
    class Meta:
        verbose_name = "Usuaria"
        ordering = ['apelido']

