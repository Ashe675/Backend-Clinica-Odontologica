# Generated by Django 5.0.4 on 2024-04-14 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta_api', '0002_remove_tratamientomodel_consulta_and_more'),
        ('recepcion', '0004_pacientemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultamodel',
            name='paciente',
        ),
        migrations.CreateModel(
            name='ExpedienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.pacientemodel', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Expediente',
                'verbose_name_plural': 'Expedientes',
                'db_table': 'Expediente',
            },
        ),
        migrations.AddField(
            model_name='consultamodel',
            name='expediente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='consulta_api.expedientemodel', verbose_name='Expediente'),
            preserve_default=False,
        ),
    ]