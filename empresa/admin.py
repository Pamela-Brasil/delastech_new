from django.contrib import admin

# Register your models here.
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'porte', 'cnpj', 'email')

admin.site.register(Empresa, EmpresaAdmin)
