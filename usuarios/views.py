from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import UsuarioPersonalizadoSerializer
from .models import UsuarioPersonalizado
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['POST'])
def login(request):
    try:
        username = request.data['username']
        user = UsuarioPersonalizado.objects.get(username=username)
        
        if not user.check_password(request.data['password']):
            return Response({
                'error': "Contraseña Incorrecta"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = UsuarioPersonalizadoSerializer(instance=user)
        return Response({
            "token": token.key,
            "user": serializer.data},
            status=status.HTTP_200_OK)
    except UsuarioPersonalizado.DoesNotExist:
        return Response({"error": "El Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({"error":"Please provide valid data"}, status=status.HTTP_400_BAD_REQUEST)
        
    


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UsuarioPersonalizadoSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message":"Token Borrado!"}, status=status.HTTP_200_OK)
