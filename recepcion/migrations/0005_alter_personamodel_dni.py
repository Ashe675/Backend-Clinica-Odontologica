# Generated by Django 5.0.4 on 2024-04-16 02:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recepcion", "0004_pacientemodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personamodel",
            name="dni",
            field=models.CharField(max_length=15, unique=True, verbose_name="Dni"),
        ),
    ]
