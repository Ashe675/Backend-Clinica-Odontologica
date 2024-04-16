from django.db import models
from recepcion.models import PacienteModel
from usuarios.models import UsuarioPersonalizado

# Create your models here.
class ExpedienteModel(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    paciente = models.OneToOneField(PacienteModel, on_delete=models.CASCADE, verbose_name='Paciente')
    class Meta:
        db_table='Expediente'
        verbose_name= 'Expediente'
        verbose_name_plural= 'Expedientes'
    
    def __str__(self) -> str:
        return f"Id Expediente: {self.id}, Paciente: {self.paciente.persona}, Fecha de creacion: {self.fecha_creacion}"

class ConsultaModel(models.Model):
    motivo_consulta = models.TextField(max_length=200, verbose_name="Motivo de la consulta")
    descripcion = models.TextField(max_length=100, verbose_name="Descripcion")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de la consulta")
    expediente = models.ForeignKey(ExpedienteModel, on_delete=models.CASCADE, verbose_name='Expediente', related_name="Expediente_Consulta")
    doctor = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, verbose_name='Doctor de la consulta')
    
    class Meta:
        db_table='Consulta'
        verbose_name= 'Consulta'
        verbose_name_plural= 'Consultas'

    def __str__(self) -> str:
        return f"ID Expediente: {self.expediente.id},Paciente: {self.expediente.paciente.persona}, Doctor: {self.doctor.persona}, Motivo de la consulta: {self.motivo_consulta}, Descripcion: {self.descripcion}, Fecha: {self.fecha} "
    
class TratamientoModel(models.Model):
    nombre = models.CharField(max_length=45, verbose_name="Nombre del tratamiento")
    precio =  models.DecimalField(verbose_name="Precio", decimal_places=2,max_digits=9)
    
    class Meta:
        db_table='Tratamiento'
        verbose_name= 'Tratamiento'
        verbose_name_plural= 'Tratamientos'

    def __str__(self) -> str:
        return f"Nombre del tratamiento: {self.nombre}, Precio: {self.precio}"
    
class TratamientoConsultaModel(models.Model):
    consulta = models.ForeignKey(ConsultaModel, verbose_name="Consulta", on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(TratamientoModel, verbose_name="Tratamiento", on_delete=models.CASCADE)
    
    class Meta:
        db_table='Tratamiento_Consulta'
        verbose_name= 'Tratamiento_Consulta'
        verbose_name_plural= 'Tratamientos_Consulta'
    
    def __str__(self) -> str:
        return f"Tratamiento: {self.tratamiento}, Consulta: {self.consulta.id}"

