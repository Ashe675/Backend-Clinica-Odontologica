from django.contrib import admin
from .models import PersonaModel, PacienteModel
# Register your models here.
admin.site.register(PersonaModel)
admin.site.register(PacienteModel)