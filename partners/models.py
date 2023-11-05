from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from users.models import Usuario

default_location = Point(-90.513228, 14.642942)

class Socio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    es_medico = models.BooleanField(default=False)
    es_flebotomista = models.BooleanField(default=False)
    es_laboratorio = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name} (socioID: {self.id})'
    
class Medico(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    socio = models.OneToOneField(Socio, on_delete=models.CASCADE)
    colegiado = models.CharField(max_length=45)
    verificado = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    def __str__(self):
        return f'Dr. {self.socio.usuario.first_name} {self.socio.usuario.last_name} (medicoID: {self.id})'

class Flebotomista(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    socio = models.OneToOneField(Socio, on_delete=models.CASCADE)
    verificado = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.socio.usuario.first_name} {self.socio.usuario.last_name} (flebotomistaID: {self.id})'

class LaboratorioClinico(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre

class SedeLaboratorioClinico(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.AutoField(primary_key=True)
    laboratorio = models.ForeignKey(LaboratorioClinico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    geolocalizacion = models.PointField(default=default_location)
    online = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre
