from django.db import models
from recepcion.models import PacienteModel
from usuarios.models import UsuarioPersonalizado

# Create your models here.
class ConsultaModel(models.Model):
    motivo_consulta = models.TextField(max_length=200, verbose_name="Motivo de la consulta")
    descripcion = models.TextField(max_length=100, verbose_name="Descripcion")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de la consulta")
    paciente = models.ForeignKey(PacienteModel, on_delete=models.CASCADE, verbose_name='Paciente')
    doctor = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, verbose_name='Doctor de la consulta')
    
    class Meta:
        db_table='Consulta'
        verbose_name= 'Consulta'
        verbose_name_plural= 'Consultas'

    def __str__(self) -> str:
        return f"Paciente: {self.paciente}, Doctor: {self.doctor}, Motivo de la consulta: {self.motivo_consulta}, Descripcion: {self.descripcion}, Fecha: {self.fecha} "
    
class TratamientoModel(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Nombre del tratamiento")
    precio =  models.DecimalField(verbose_name="Precio", decimal_places=2,max_digits=9)
    consulta = models.ManyToManyField(ConsultaModel,related_name="Tratamientos_Consulta", verbose_name="Consulta")
    
    class Meta:
        db_table='Tratamiento'
        verbose_name= 'Tratamiento'
        verbose_name_plural= 'Tratamientos'

    def __str__(self) -> str:
        return f"Nombre del tratamiento: {self.nombre}, Precio: {self.precio}"