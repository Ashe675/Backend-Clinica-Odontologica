from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import generics
from django.http import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from recepcion.models import (
    PacienteModel,
    PersonaModel
)
from .serializer import (
    PacienteModelSerializer,
    PersonaModelSerializer,
    ViewPacientesSerializer,
    ViewPacienteSerializer
)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_pacient(request):
    try:
        #Create Persona
        persona_serializer = PersonaModelSerializer(data=request.data)
        persona_serializer.is_valid(raise_exception=True)
        persona = persona_serializer.save()

        # Recibir id persona y agregarlo a la data
        paciente_data = request.data
        paciente_data['persona'] = persona.id

        #Create Paciente
        paciente_serializer = PacienteModelSerializer(data=paciente_data)
        paciente_serializer.is_valid(raise_exception=True)
        paciente = paciente_serializer.save()

        # Retornar=el ID del paciente y el nombre completo 
        return Response({
            'id_paciente': paciente.id,
            'nombre_completo_persona': f'{persona.primer_nombre} {persona.primer_apellido}',
            'dni':persona.dni
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# Create your views heres
class PacienteModelAPIview(generics.ListAPIView):
    queryset= PacienteModel.objects.all()
    serializer_class=ViewPacientesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

class PacienteModelAPIRetrieve(generics.RetrieveAPIView):
    queryset= PacienteModel.objects.all()
    serializer_class=ViewPacienteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Paciente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

# ViewSets
# class PacienteModelViewSet(viewsets.ModelViewSet):
#     queryset=PacienteModel.objects.all()
#     serializer_class=PacienteModelSerializer