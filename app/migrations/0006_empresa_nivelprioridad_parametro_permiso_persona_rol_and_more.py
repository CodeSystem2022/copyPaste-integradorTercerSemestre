# Generated by Django 4.1.7 on 2023-06-19 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_ciudad_capital_dpto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresa_id', models.AutoField(primary_key=True, serialize=False)),
                ('empresa_descripcion', models.CharField(max_length=50)),
                ('empresa_direccion', models.CharField(blank=True, max_length=50)),
                ('empresa_telefono', models.CharField(blank=True, max_length=15)),
                ('empresa_correo', models.CharField(blank=True, max_length=25)),
                ('empresa_ruc', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='NivelPrioridad',
            fields=[
                ('nivel_prioridad_id', models.AutoField(primary_key=True, serialize=False)),
                ('nivel_prioridad_condicion', models.CharField(max_length=50)),
                ('nivel_prioridad_prioridad', models.SmallIntegerField()),
                ('nivel_prioridad_estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('parametro_id', models.AutoField(primary_key=True, serialize=False)),
                ('parametro_descripcion', models.CharField(max_length=25)),
                ('parametro_tipo_dato', models.CharField(max_length=25)),
                ('parametro_valor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('permiso_id', models.AutoField(primary_key=True, serialize=False)),
                ('permiso_descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('persona_id', models.AutoField(primary_key=True, serialize=False)),
                ('persona_cedula', models.CharField(max_length=15)),
                ('persona_nombre', models.CharField(max_length=50)),
                ('persona_apellido', models.CharField(max_length=50)),
                ('persona_direccion', models.CharField(max_length=50)),
                ('persona_telefono', models.CharField(max_length=15)),
                ('persona_correo', models.CharField(max_length=25)),
                ('ciudad_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_descripcion', models.CharField(max_length=25)),
                ('permiso_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('servicio_id', models.AutoField(primary_key=True, serialize=False)),
                ('servicio_descripcion', models.CharField(max_length=50)),
                ('servicio_estado', models.BooleanField(default=True)),
                ('servicio_cantidad_cola', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('sexo_id', models.AutoField(primary_key=True, serialize=False)),
                ('sexo_descripcion', models.CharField(max_length=15)),
                ('sexo_abreviatura', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_nro', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('tipo_persona_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_persona_descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_nombre', models.CharField(max_length=25)),
                ('usuario_fecha_alta', models.DateField()),
                ('usuario_fecha_baja', models.DateField(blank=True, null=True)),
                ('usuario_estado', models.BooleanField(default=True)),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.persona')),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.rol')),
            ],
        ),
        migrations.CreateModel(
            name='PersonaSet',
            fields=[
                ('persona_set_id', models.AutoField(primary_key=True, serialize=False)),
                ('persona_set_nombre', models.CharField(max_length=35)),
                ('persona_set_ruc', models.CharField(max_length=15)),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.persona')),
                ('tipo_persona_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.tipopersona')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.sexo'),
        ),
        migrations.CreateModel(
            name='Cola',
            fields=[
                ('cola_id', models.AutoField(primary_key=True, serialize=False)),
                ('cola_ticket_nro', models.SmallIntegerField()),
                ('cola_fecha_hora_ingreso', models.DateField()),
                ('cola_fecha_hora_salida', models.DateField(blank=True, null=True)),
                ('cola_fecha_hora_atencion', models.DateField(blank=True, null=True)),
                ('cola_estado', models.CharField(max_length=10)),
                ('nivel_prioridad_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.nivelprioridad')),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.persona')),
                ('servicio_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.servicio')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.usuario')),
            ],
        ),
    ]
