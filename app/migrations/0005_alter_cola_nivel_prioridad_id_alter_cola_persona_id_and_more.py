# Generated by Django 4.1.7 on 2023-06-17 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cola_nivel_prioridad_id_alter_cola_persona_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cola',
            name='nivel_prioridad_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.nivelprioridad'),
        ),
        migrations.AlterField(
            model_name='cola',
            name='persona_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.persona'),
        ),
        migrations.AlterField(
            model_name='cola',
            name='servicio_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.servicio'),
        ),
    ]