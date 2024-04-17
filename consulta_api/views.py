from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from paciente_api.serializer import PacienteModelSerializer, ViewPacienteSerializer
from usuarios.models import UsuarioPersonalizado 
from recepcion.models import PacienteModel
from usuarios.serializer import UsuarioPersonalizadoSerializer
from .serializer import TratamientoModelSerializer, ConsultaModelSerializer, ConsultaModelSerializer2 ,ExpedienteModelSerializer, TratamientoConsultaModelSerializer
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
        tratamientos =  request.data.pop('tratamientos')
        if serializerConsulta.is_valid():
            doctor = request.user
            consulta = request.data
            consulta['doctor'] = doctor
            del consulta['dniPaciente']
            expediente,created = ExpedienteModel.objects.get_or_create(paciente = paciente)
            consulta['expediente'] = expediente
            newConsulta = ConsultaModel.objects.create(**consulta)
            serializerConsulta = ConsultaModelSerializer(instance=newConsulta)
            serializerConsulta_data = serializerConsulta.data
            if tratamientos:
                for tratamiento_index in tratamientos:
                    TratamientoModel.objects.get(id=tratamiento_index)
                    TratamientoConsultaModel.objects.create(consulta = newConsulta, tratamiento_id = tratamiento_index)
                tratamientos_consultas = TratamientoConsultaModel.objects.filter(consulta=newConsulta)
                serializer_tratamientos_consultas = TratamientoConsultaModelSerializer(tratamientos_consultas, many=True)
                serializerConsulta_data['tratamientos'] = serializer_tratamientos_consultas.data
            else:
                serializerConsulta_data['tratamientos'] = []
            return Response(serializerConsulta_data,status=status.HTTP_200_OK)
        return Response(serializerConsulta.errors, status=status.HTTP_400_BAD_REQUEST)
    except PacienteModel.DoesNotExist:
        return Response({"error": "El paciente no existe"}, status=status.HTTP_404_NOT_FOUND)
    except TratamientoModel.DoesNotExist:
        return Response({"error": "Un tratamiento no existe"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def expediente(request):
    try:
        paciente = PacienteModel.objects.get(persona__dni=request.data['dniPaciente'])
        expediente, created = ExpedienteModel.objects.get_or_create(paciente=paciente)
        expediente_serializer = ExpedienteModelSerializer(instance=expediente)
        expediente_data = expediente_serializer.data
        expediente_data['paciente'] = ViewPacienteSerializer(paciente).data
        try:
            consultas = ConsultaModel.objects.filter(expediente=expediente)
            consultas_serializer = ConsultaModelSerializer2(consultas, many=True)
            expediente_data['consultas'] = consultas_serializer.data
        except ConsultaModel.DoesNotExist:
            expediente_data['consultas'] = []
        return Response(expediente_data,status=status.HTTP_200_OK)
    except PacienteModel.DoesNotExist:
        return Response({"error": "El paciente no existe"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e) }, status=status.HTTP_400_BAD_REQUEST)


class TratamientoModelAPIList(generics.ListAPIView):
    queryset = TratamientoModel.objects.all()
    serializer_class = TratamientoModelSerializer
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
