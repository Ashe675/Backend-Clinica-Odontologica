from rest_framework import serializers
from .models import (
    UsuarioPersonalizado
)

class UsuarioPersonalizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioPersonalizado
        fields=['id','username','email']