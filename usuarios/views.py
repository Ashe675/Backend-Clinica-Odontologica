from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def signin(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm
        }
        return render(request,'signin.html', context)
    else:
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])
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