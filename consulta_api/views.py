from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from paciente_api.serializer import PacienteModelSerializer, ViewPacienteSerializer
from usuarios.models import UsuarioPersonalizado 
from recepcion.models import PacienteModel
from usuarios.serializer import UsuarioPersonalizadoSerializer
from .serializer import( TratamientoModelSerializer, ConsultaModelSerializer, ConsultaModelSerializer2 ,
                        ExpedienteModelSerializer, TratamientoConsultaModelSerializer, FacturaModelSerializer)
from .models import TratamientoModel, ConsultaModel, ExpedienteModel, TratamientoConsultaModel, FacturaModel
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

#Crear la factura al tener una nueva consulta
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def crear_factura(request):
    consulta_Id= request.query_params.get('consulta')
    try:
        consulta= ConsultaModel.objects.get(id=consulta_Id)
    except ConsultaModel.DoesNotExist:
        return Response({'msg':'Consulta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    monto= 0
    tratamientos= TratamientoConsultaModel.objects.filter(consulta=consulta)
    for tratamiento in tratamientos:
        monto+=tratamiento.tratamiento.precio

    factura={'consulta':consulta_Id, 'monto':monto}
    nueva_factura=FacturaModelSerializer(data=factura)
    if nueva_factura.is_valid():
            nueva_factura.save()
            return Response(nueva_factura.data, status=status.HTTP_201_CREATED)
    return Response(nueva_factura.errors, status=status.HTTP_400_BAD_REQUEST)


#Ver la factura
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ver_factura(request):
    #print(request.user)
    consulta_Id= request.query_params.get('consulta_id')
    try:
        consulta= ConsultaModel.objects.get(id=consulta_Id)
    except ConsultaModel.DoesNotExist:
        return Response({'msg':'Consulta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    

    paciente= consulta.expediente.paciente.persona

    doctor_id= consulta.doctor.id
    doctor=get_object_or_404(UsuarioPersonalizado, id=doctor_id)

    factura= FacturaModel.objects.filter(consulta=consulta).first()

    recepcionista_id= request.user.id
    recepcionista = get_object_or_404(UsuarioPersonalizado, id=recepcionista_id)
    #print(recepcionista.username)
    if not factura:
        return Response({'msg': 'Factura no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    if not factura.estado:
        #factura.estado= 1
        factura.recepcionista=recepcionista
        factura.fecha_emision= datetime.today().strftime("%Y-%m-%d")
        factura.save()

    #datos recepcionista
    recepcionista_data={'nombre':recepcionista.persona.primer_nombre + ' ' +recepcionista.persona.primer_apellido}

    #datos doctor
    doctor_data={'nombre':doctor.username}

    #traer tratamientos
    tratamientos= TratamientoConsultaModel.objects.filter(consulta=consulta)
    nombres_tratamientos= [tratamiento.tratamiento.nombre for tratamiento in tratamientos]


    data = {
        "paciente":{"nombre":paciente.primer_nombre +' '+ paciente.primer_apellido,"dni":paciente.dni},
        "doctor": doctor_data,
        "tratamientos": nombres_tratamientos,
        "factura": {
            "consulta": factura.consulta.id,
            "estado": factura.estado,
            "fecha_emision": factura.fecha_emision,
            "monto": factura.monto,
            "recepcionista": recepcionista_data,
        }
    }

    return Response(data, status=status.HTTP_200_OK)