from django.contrib.auth.models import AbstractUser
from django.db import models
from recepcion.models import PersonaModel

class Rol(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class UsuarioPersonalizado(AbstractUser):
    persona = models.ForeignKey(PersonaModel, on_delete=models.CASCADE, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, related_name='Rol')

    def __str__(self):
        return self.username
