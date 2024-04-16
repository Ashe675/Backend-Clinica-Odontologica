from django.urls import path
from . import views
    
urlpatterns = [
    path('create/',views.create_consulta, name='create_consulta'),
    path('',views.expediente, name='expediente'),
]

