from rest_framework import serializers
from .models import ConsultaModel, TratamientoModel, TratamientoConsultaModel

class ConsultaModelSerializer(serializers.ModelSerializer):
    paciente = serializers.CharField(source='paciente.persona.primer_nombre',read_only=True)
    doctor = serializers.CharField(source='doctor.persona.primer_nombre',read_only=True)
    
    class Meta:
        model = ConsultaModel
        fields = ['motivo_consulta', 'descripcion', 'fecha', 'paciente', 'doctor']

class TratamientoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoModel
        fields = ['nombre','precio']
        
class TratamientoConsultaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoConsultaModel
        fields = '__all__'