from django.urls import path
from . import views
    
urlpatterns = [
    path('create-consulta/',views.create_consulta, name='create_consulta'),
    path('expediente/',views.expediente, name='expediente'),
    path('tratamientos/',views.TratamientoModelAPIList.as_view(), name='expediente'),
    path('facturas/', views.ver_factura, name='ver_factura'),
    path('facturas/pago/', views.pagar_factura, name='pago_factura'),
    path('facturas/pendientes', views.FacturasPendienteAPIList.as_view(), name='facturas_pendientes'),
]

