# Generated by Django 4.1.7 on 2023-06-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='departamento_abreviatura',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
