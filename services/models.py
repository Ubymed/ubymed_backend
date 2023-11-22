from django.db import models
from partners.models import SedeLaboratorioClinico

class Servicio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    url = models.CharField(max_length=45)
    sort_index = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.nombre} (id: {self.id})'

class ConsultaMedica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    descripcion_larga = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=45)
    sort_index = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class PruebaLaboratorio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    descripcion = models.TextField()
    sku = models.CharField(max_length=45)
    preparacion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    laboratorio = models.ForeignKey(SedeLaboratorioClinico, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre