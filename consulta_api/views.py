from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from usuarios.models import UsuarioPersonalizado 
from recepcion.models import PacienteModel
from usuarios.serializer import UsuarioPersonalizadoSerializer
from .serializer import TratamientoModelSerializer, ConsultaModelSerializer
from .models import TratamientoModel, ConsultaModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_consulta(request):
    try:
        paciente = get_object_or_404(PacienteModel,persona__dni=request.data['dniPaciente'])
        serializerConsulta = ConsultaModelSerializer(data = request.data)
        if serializerConsulta.is_valid():
            doctor = request.user
            consulta = request.data
            consulta['doctor'] = doctor
            del consulta['dniPaciente']
            consulta['paciente'] = paciente
            print(type(consulta))
            newConsulta = ConsultaModel.objects.create(**consulta)
            newConsulta.save()
            serializerConsulta = ConsultaModelSerializer(instance=newConsulta)
            return Response(serializerConsulta.data,status=status.HTTP_200_OK)
        return Response(serializerConsulta.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"error":"Please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def consultas(request):
    try:
        paciente = get_object_or_404(PacienteModel,persona__dni=request.data['dniPaciente'])
        consultas = ConsultaModel.objects.filter(paciente=paciente.id)
        consultasSerializer = []
        for consulta in consultas:
            consultaSerializer = ConsultaModelSerializer(instance=consulta)
            consultasSerializer.append(consultaSerializer.data)
        return Response(consultasSerializer,status=status.HTTP_200_OK)
    except:
        return Response({"error":"Please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)

