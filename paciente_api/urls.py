from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    PersonaModelAPICreate,
    PersonalModelAPIDestroy,
    PacienteModelViewSet
)

router= DefaultRouter()
router.register('pacientes', PacienteModelViewSet, basename='pacientes')

urlpatterns = [
    path('persona-create/', PersonaModelAPICreate.as_view(), name='persona_create')
]

urlpatterns += router.urls