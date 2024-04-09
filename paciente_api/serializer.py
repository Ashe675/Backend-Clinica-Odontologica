from rest_framework import serializers
from recepcion.models import (
    PersonaModel,
    PacienteModel
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