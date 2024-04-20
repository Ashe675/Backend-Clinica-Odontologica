from rest_framework import serializers
from recepcion.models import (
    PersonaModel,
    PacienteModel,
)


#Serializadores
class PersonaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonaModel
        fields='__all__'

class PacienteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=PacienteModel
        fields='__all__'

class ViewPacientesSerializer(serializers.ModelSerializer):
    primer_nombre = serializers.CharField(source='persona.primer_nombre', read_only=True)
    primer_apellido= serializers.CharField(source='persona.primer_apellido', read_only=True)
    dni=serializers.CharField(source='persona.dni', read_only=True)
    class Meta:
        model=PacienteModel
        exclude= ['persona']

class ViewPacienteSerializer(serializers.ModelSerializer):
    primer_nombre = serializers.CharField(source='persona.primer_nombre', read_only=True)
    primer_apellido= serializers.CharField(source='persona.primer_apellido', read_only=True)
    dni=serializers.CharField(source='persona.dni', read_only=True)
    class Meta:
        model=PacienteModel
        exclude= ['persona']

