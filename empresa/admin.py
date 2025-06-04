from django.contrib import admin

# Register your models here.
from .models import Empresa

admin.site.register(Empresa)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'porte', 'cnpj', 'contato')
