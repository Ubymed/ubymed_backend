from django.contrib import admin
from .models import Socio, Medico, LaboratorioClinico ,SedeLaboratorioClinico, Flebotomista

# Register your models here.
admin.site.register(Socio)
admin.site.register(Medico)
admin.site.register(Flebotomista)
admin.site.register(LaboratorioClinico)
admin.site.register(SedeLaboratorioClinico)