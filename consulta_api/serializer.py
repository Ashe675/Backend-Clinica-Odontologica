from rest_framework import serializers
from .models import ConsultaModel, TratamientoModel, TratamientoConsultaModel, ExpedienteModel

class ConsultaModelSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='expediente.paciente.persona.primer_nombre',read_only=True)
    doctor = serializers.CharField(source='doctor.persona.primer_nombre',read_only=True)
    expediente_id = serializers.IntegerField(source='expediente.id',read_only=True)
    
    class Meta:
        model = ConsultaModel
        fields = ['motivo_consulta', 'descripcion', 'fecha', 'paciente', 'doctor', 'expediente_id']

class TratamientoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoModel
        fields = ['nombre','precio']
        
class TratamientoConsultaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoConsultaModel
        fields = '__all__'
        

class ExpedienteModelSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='paciente.persona.primer_nombre',read_only=True)
    id_expediente = serializers.IntegerField(source = 'id', read_only=True) 
    class Meta:
        model = ExpedienteModel
        fields = ['id_expediente','fecha_creacion','paciente']