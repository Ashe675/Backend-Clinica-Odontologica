# Generated by Django 5.0.4 on 2024-04-09 15:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recepcion", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personamodel",
            name="dni",
        ),
    ]