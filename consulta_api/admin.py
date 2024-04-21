from django.contrib import admin
from .models import ConsultaModel, TratamientoModel,TratamientoConsultaModel, ExpedienteModel, FacturaModel

# Register your models here.
admin.site.register(ConsultaModel)
admin.site.register(TratamientoModel)
admin.site.register(TratamientoConsultaModel)
admin.site.register(ExpedienteModel)
admin.site.register(FacturaModel)