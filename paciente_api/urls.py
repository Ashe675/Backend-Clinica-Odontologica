from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    PacienteModelAPIview,
    PacienteModelViewSet,
    PacienteModelAPIRetrieve,
    create_pacient
)

router= DefaultRouter()
router.register('pacientes', PacienteModelViewSet, basename='pacientes')

urlpatterns = [
    path('pacientes/', PacienteModelAPIview.as_view(), name='view_pacientes'),
    path('paciente/', PacienteModelAPIRetrieve.as_view(), name='view_paciente'),
    path('paciente-create/', create_pacient, name='crear_paciente')
]

urlpatterns += router.urls