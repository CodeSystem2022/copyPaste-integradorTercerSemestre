# Generated by Django 4.1.7 on 2023-06-17 21:12
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='persona_fecha_nacimineto',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]


