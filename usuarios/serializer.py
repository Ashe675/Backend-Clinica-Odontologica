from rest_framework import serializers
from .models import (
    UsuarioPersonalizado
)

class UsuarioPersonalizadoSerializer(serializers.ModelSerializer):
    rol = serializers.CharField(source='rol.description', read_only=True)
    class Meta:
        model= UsuarioPersonalizado
        fields=['id','username','email','password','rol']