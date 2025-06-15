from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import empresa

@receiver(post_save, sender=User)
def criar_perfil_empresa(sender, instance, created, **kwargs):
    if created:
        empresa.objects.create(user=instance)