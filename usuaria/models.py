from django.db import models

# Create your models here.
class Usuaria(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email =  models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    escolaridade = models.CharField(max_length=30)
    idiomas = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=3000)
    apelido = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.apelido}"
    
    class Meta:
        verbose_name = "Usuaria"
        ordering = ['apelido']