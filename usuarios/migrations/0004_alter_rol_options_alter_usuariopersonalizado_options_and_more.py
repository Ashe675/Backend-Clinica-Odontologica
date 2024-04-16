# Generated by Django 5.0.4 on 2024-04-14 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0004_pacientemodel'),
        ('usuarios', '0003_alter_usuariopersonalizado_rol'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rol',
            options={'verbose_name': 'Rol', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='usuariopersonalizado',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='rol',
            name='description',
            field=models.CharField(max_length=30, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Persona', to='recepcion.personamodel', verbose_name='Persona'),
        ),
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Rol', to='usuarios.rol', verbose_name='Rol'),
        ),
        migrations.AlterModelTable(
            name='rol',
            table='Rol',
        ),
        migrations.AlterModelTable(
            name='usuariopersonalizado',
            table='Usuario',
        ),
    ]