from django.contrib import admin

# Register your models here.
from .models import Usuaria, Idioma

admin.site.register(Usuaria)
admin.site.register(Idioma)
