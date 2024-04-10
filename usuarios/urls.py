from django.urls import path
from . import views
app_name = 'usuarios'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]