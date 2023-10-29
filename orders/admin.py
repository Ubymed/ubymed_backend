from django.contrib import admin
from .models import Orden, OrdenConsultaMedica, OrdenPruebaLaboratorio, DetalleOrdenLaboratorio, RegistroConsultaMedica, RegistroPruebaLaboratorio

# Register your models here.
admin.site.register(Orden)
admin.site.register(OrdenConsultaMedica)
admin.site.register(OrdenPruebaLaboratorio)
admin.site.register(DetalleOrdenLaboratorio)
admin.site.register(RegistroConsultaMedica)
admin.site.register(RegistroPruebaLaboratorio)