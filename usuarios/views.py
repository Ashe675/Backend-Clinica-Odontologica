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
    user = get_object_or_404(UsuarioPersonalizado,username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({
            'error':"Invalid Password"}, status= status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UsuarioPersonalizadoSerializer(instance=user)
    return Response({
        "token": token.key,
        "user": serializer.data},
        status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UsuarioPersonalizadoSerializer(instance=request.user)
    
    #return Response("You are login with {}".format(request.user.username), status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)


