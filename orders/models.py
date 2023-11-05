from tokenize import Pointfloat
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from users.models import Usuario
from partners.models import Socio, Medico, SedeLaboratorioClinico
from services.models import ConsultaMedica, PruebaLaboratorio
from services.models import Servicio

default_location = Point(-90.513228, 14.642942)

class Orden(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.DO_NOTHING)
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    opciones_estado = [
        ("incompleta", "Incompleta"),
        ("completa", "Completa"),
        ("cancelada", "Cancelada")
    ]
    estado = models.CharField(
        choices=opciones_estado,
        default="incompleta"
    )

    def __str__(self):
        return f'Orden {self.id} - Usuario: {self.usuario.first_name} {self.usuario.first_name}'
    
class OrdenConsultaMedica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    orden_id = models.ForeignKey(Orden, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    catalogo_consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    estado_detalle = models.CharField(max_length=45)
    detalles = models.TextField()
    lugar = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    geolocalizacion = models.PointField(default=default_location)
    paciente_nombre = models.CharField(max_length=45)
    paciente_apellido = models.CharField(max_length=45)
    paciente_edad = models.CharField(max_length=45)
    paciente_dpi = models.CharField(max_length=45)
    paciente_telefono = models.CharField(max_length=45)
    paciente_email = models.CharField(max_length=45, null=True, blank=True)
    paciente_sexo = models.CharField(max_length=1)

    def __str__(self):
        return f"Orden de Consulta {self.id}"
    
class OrdenPruebaLaboratorio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    orden_id = models.ForeignKey(Orden, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(SedeLaboratorioClinico, on_delete=models.CASCADE)
    estado_detalle = models.CharField(max_length=45)
    lugar = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    geolocalizacion = models.PointField(default=default_location)
    paciente_nombre = models.CharField(max_length=45)
    paciente_apellido = models.CharField(max_length=45)
    paciente_edad = models.CharField(max_length=45)
    paciente_dpi = models.CharField(max_length=45)
    paciente_telefono = models.CharField(max_length=45)
    paciente_email = models.CharField(max_length=45, null=True, blank=True)
    paciente_sexo = models.CharField(max_length=1)

    def __str__(self):
        return f"Orden de Laboratorio {self.id}"
    
class DetalleOrdenLaboratorio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    orden_id = models.ForeignKey(Orden, on_delete=models.CASCADE)
    prueba_laboratorio = models.ForeignKey(PruebaLaboratorio, on_delete=models.CASCADE)
    def __str__(self):
        return f"Detalle de Laboratorio para Orden {self.orden_id.id}"

class RegistroConsultaMedica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    motivo = models.TextField(null=True)
    historia = models.TextField(null=True)
    exploracion = models.TextField(null=True)
    diagnostico = models.TextField()
    plan = models.TextField()
    orden_id = models.ForeignKey(OrdenConsultaMedica, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    comentario = models.TextField(null=True)

    def __str__(self):
        return f"Registro de Consulta para Orden {self.orden.id}"
    
class RegistroPruebaLaboratorio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    comentario = models.TextField(null=True)
    orden_id = models.ForeignKey(OrdenPruebaLaboratorio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro de Laboratorio para Orden {self.orden.id}"