from rest_framework import serializers
from .models import ConsultaModel, TratamientoModel, TratamientoConsultaModel, ExpedienteModel, FacturaModel

class ConsultaModelSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='expediente.paciente.persona.primer_nombre',read_only=True)
    doctor = serializers.CharField(source='doctor.persona.primer_nombre',read_only=True)
    expediente_id = serializers.IntegerField(source='expediente.id',read_only=True)
    
    class Meta:
        model = ConsultaModel
        fields = ['id','motivo_consulta', 'descripcion', 'fecha', 'paciente', 'doctor', 'expediente_id']

class TratamientoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoModel
        fields = ['id','nombre','precio']
        
class TratamientoConsultaModelSerializer(serializers.ModelSerializer):
    consulta_id = serializers.IntegerField(source='consulta.id',read_only=True)
    tratamiento = serializers.CharField(source='tratamiento.nombre',read_only=True)
    precio_tratamiento = serializers.IntegerField(source='tratamiento.precio',read_only=True)
    class Meta:
        model = TratamientoConsultaModel
        fields = ['consulta_id', 'tratamiento', 'precio_tratamiento']
        
class ConsultaModelSerializer2(serializers.ModelSerializer):
    paciente = serializers.CharField(source='expediente.paciente.persona.primer_nombre',read_only=True)
    doctor = serializers.CharField(source='doctor.persona.primer_nombre',read_only=True)
    expediente_id = serializers.IntegerField(source='expediente.id',read_only=True)
    tratamientos = TratamientoConsultaModelSerializer(many=True, read_only=True)
    class Meta:
        model = ConsultaModel
        fields = ['id','motivo_consulta', 'descripcion', 'fecha', 'paciente', 'doctor', 'expediente_id', 'tratamientos']


class ExpedienteModelSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='paciente.persona.primer_nombre',read_only=True)
    id_expediente = serializers.IntegerField(source = 'id', read_only=True) 
    class Meta:
        model = ExpedienteModel
        fields = ['id_expediente','fecha_creacion','paciente']

#Serializdadores Facturacion

#para crear una factura con la consulta
class FacturaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaModel
        fields = ['consulta','monto']