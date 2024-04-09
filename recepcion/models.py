from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class PersonaModel(models.Model):
    dni=models.CharField(max_length=15, verbose_name='Dni', null=False, blank=False)
    primer_nombre = models.CharField(max_length=75, verbose_name="Primer Nombre")
    segundo_nombre = models.CharField(max_length=75, null=True,blank=True ,verbose_name="Segundo Nombre")
    primer_apellido = models.CharField(max_length=75, verbose_name="Primer Apellido")
    segundo_apellido = models.CharField(max_length=75, null=True, blank=True ,verbose_name="Segundo Apellido")

    class Meta:
        db_table='Persona'
        verbose_name= 'Persona'
        verbose_name_plural= 'Personas'

    def __str__(self) -> str:
        return f'{self.primer_nombre} {self.primer_apellido}'

class PacienteModel(models.Model):
    correo=models.EmailField(null=False, verbose_name='Correo')
    telefono=models.CharField(max_length=15, verbose_name='Telefono')
    fecha_nacimiento=models.DateField(verbose_name='Fecha Nacimiento', null=False, blank=False)
    direccion= models.TextField(max_length=100, verbose_name='Direccion')
    genero= models.CharField(max_length=1, verbose_name='Genero')
    persona= models.OneToOneField(PersonaModel, verbose_name='Persona', related_name='pacientes', on_delete=models.CASCADE)

    class Meta:
        db_table='Paciente'
        verbose_name= 'Paciente'
        verbose_name_plural= 'Pacientes'

    def __str__(self) -> str:
        return self.correo
    
# class UsuarioModel(models.Model):
#     username=models.CharField(max_length=75, null=False, blank=False, verbose_name='Nombre Usuario')
#     contrasenia= models.CharField(max_length=120, null=False, blank=False, verbose_name='Contrasenia')
#     persona= models.OneToOneField(PersonaModel, verbose_name='Persona', related_name='usuarios', on_delete=models.CASCADE)

#     def save(self, *args, **kwargs):
#         # Encripta la contraseña antes de guardarla
#         self.contrasenia = make_password(self.contrasenia)
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table='Usuario'
#         verbose_name= 'Usuario'
#         verbose_name_plural= 'Usuarios'

#     def __str__(self) -> str:
#         return self.username