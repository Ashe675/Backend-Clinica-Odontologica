from django.contrib.auth.models import AbstractUser
from django.db import models
from recepcion.models import PersonaModel

class Rol(models.Model):
    description = models.CharField(max_length=30,verbose_name="Descripcion")

    class Meta:
        db_table='Rol'
        verbose_name= 'Rol'
        verbose_name_plural= 'Roles'

    def __str__(self):
        return self.description

class UsuarioPersonalizado(AbstractUser):
    persona = models.ForeignKey(PersonaModel, on_delete=models.CASCADE, null=True, related_name='Persona', verbose_name="Persona")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, related_name='Rol', verbose_name="Rol")

    class Meta:
        db_table='Usuario'
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'

    # def save(self, *args, **kwargs):
    #     if self.password:
    #         self.set_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.username
