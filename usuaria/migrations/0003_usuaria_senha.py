# Generated by Django 4.2.23 on 2025-06-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuaria', '0002_idioma_alter_usuaria_cnpj_alter_usuaria_escolaridade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuaria',
            name='senha',
            field=models.CharField(default='senha123', max_length=128),
        ),
    ]
