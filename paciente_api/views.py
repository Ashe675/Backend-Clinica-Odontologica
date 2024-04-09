from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from recepcion.models import (
    PacienteModel,
    PersonaModel
)
from .serializer import (
    PacienteModelSerializer,
    PersonaModelSerializer
)

# Create your views heres
class PersonaModelAPICreate(generics.CreateAPIView):
    queryset= PersonaModel.objects.all()
    serializer_class=PersonaModelSerializer

class PersonalModelAPIDestroy(generics.DestroyAPIView):
    queryset= PersonaModel.objects.all()
    serializer_class=PersonaModelSerializer

#ViewSets
class PacienteModelViewSet(viewsets.ModelViewSet):
    queryset=PacienteModel.objects.all()
    serializer_class=PacienteModelSerializer