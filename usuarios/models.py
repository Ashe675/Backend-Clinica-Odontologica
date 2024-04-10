from django.contrib.auth.models import AbstractUser
from django.db import models
from recepcion.models import PersonaModel

class Rol(models.Model):
    description = models.CharField(max_length=30)

class UsuarioPersonalizado(AbstractUser):
    persona = models.ForeignKey(PersonaModel, on_delete=models.CASCADE, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
