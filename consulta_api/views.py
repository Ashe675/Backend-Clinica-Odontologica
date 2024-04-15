from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from paciente_api.serializer import PacienteModelSerializer
from usuarios.models import UsuarioPersonalizado 
from recepcion.models import PacienteModel
from usuarios.serializer import UsuarioPersonalizadoSerializer
from .serializer import TratamientoModelSerializer, ConsultaModelSerializer, ExpedienteModelSerializer
from .models import TratamientoModel, ConsultaModel, ExpedienteModel, TratamientoConsultaModel
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
            expediente,created = ExpedienteModel.objects.get_or_create(paciente = paciente)
            consulta['expediente'] = expediente
            newConsulta = ConsultaModel.objects.create(**consulta)
            newConsulta.save()
            serializerConsulta = ConsultaModelSerializer(instance=newConsulta)
            return Response(serializerConsulta.data,status=status.HTTP_200_OK)
        return Response(serializerConsulta.errors, status=status.HTTP_400_BAD_REQUEST)
    except PacienteModel.DoesNotExist:
        return Response({"error": "El paciente no existe"}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({"error":"Please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def expediente(request):
    try:
        paciente = PacienteModel.objects.get(persona__dni=request.data['dniPaciente'])
        expediente, created = ExpedienteModel.objects.get_or_create(paciente=paciente)
        expediente_serializer = ExpedienteModelSerializer(instance=expediente)
        expediente_data = expediente_serializer.data
        expediente_data['paciente'] = PacienteModelSerializer(paciente).data
        try:
            consultas = ConsultaModel.objects.filter(expediente=expediente)
            consultas_serializer = ConsultaModelSerializer(consultas, many=True)
            expediente_data['consultas'] = consultas_serializer.data
        except ConsultaModel.DoesNotExist:
            expediente_data['consultas'] = []
        return Response(expediente_data,status=status.HTTP_200_OK)
    except PacienteModel.DoesNotExist:
        return Response({"error": "El paciente no existe"}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({"error":"Please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)

