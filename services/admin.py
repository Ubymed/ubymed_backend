from django.contrib import admin
from .models import ConsultaMedica, PruebaLaboratorio, Servicio

# Register your models here.
admin.site.register(Servicio)
admin.site.register(ConsultaMedica)
admin.site.register(PruebaLaboratorio)