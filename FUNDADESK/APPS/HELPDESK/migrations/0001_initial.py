# Generated by Django 3.1.7 on 2021-02-27 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('inc_id', models.AutoField(primary_key=True, serialize=False)),
                ('inc_tipo', models.CharField(choices=[('00', 'Consulta'), ('01', 'Error'), ('02', 'Cotización')], default='00', max_length=2)),
                ('inc_descripcion', models.CharField(max_length=255)),
                ('inc_detalle', models.TextField()),
                ('inc_estado', models.CharField(choices=[('00', 'Sin asignar'), ('01', 'Asignado'), ('02', 'Resuelto'), ('XX', 'Cancelado'), ('DV', 'Devuelto')], default='00', max_length=2)),
                ('inc_fecha_apertura', models.DateField(auto_now_add=True)),
                ('inc_fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('inc_fecha_cierre', models.DateField(blank=True, null=True)),
                ('inc_responsable', models.ForeignKey(blank=True, limit_choices_to={'group__name': 'Agentes'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_agente', to=settings.AUTH_USER_MODEL)),
                ('inc_usuario', models.ForeignKey(limit_choices_to={'group_name': 'Clientes'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User_cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
