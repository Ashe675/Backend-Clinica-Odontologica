from django.contrib import admin
from .models import ConsultaModel, TratamientoModel,TratamientoConsultaModel

# Register your models here.
admin.site.register(ConsultaModel)
admin.site.register(TratamientoModel)
admin.site.register(TratamientoConsultaModel)