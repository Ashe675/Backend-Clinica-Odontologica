from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .serializer import (
    UsuarioPersonalizadoSerializer
)
from .models import UsuarioPersonalizado

@api_view(['POST'])
def login(request):
    print(request.data)
    user= get_object_or_404(UsuarioPersonalizado, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error":"Password incorrecto"})
    
    token,created= Token.objects.get_or_create(user=user)
    serializer= UsuarioPersonalizadoSerializer(instance=user)

    return Response({"token":token.key, "user":serializer.data})

@api_view(['POST'])
def register(request):
    return Response({})


# Create your views here.
@csrf_exempt
def signin(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm
        }
        return render(request,'signin.html', context)
    else:
        data = json.loads(request.body)
        print(data)
        username = data.get('username')
        password = data.get('password')
        print(username)
        print(password)
        user = authenticate(request, username = username, password = password)
        if user is None:
            context = {
            'form': AuthenticationForm,
            'error': 'Username or password is incorrect'
            }
            #return render(request,'signin.html', context)
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
        else:
            login(request, user)
            #return render(request,'login.html')
            return JsonResponse({'token': 'your_generated_token'})

@login_required
def home(request):
    return render(request,'login.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')