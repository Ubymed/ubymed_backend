from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone  # Importa la librería timezone
from .managers import CustomUserManager

class Usuario(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=45)
    masculino = 'm'
    femenino = 'f'
    opciones_sexo = [
        (masculino, 'Masculino'),
        (femenino, 'Femenino'),
    ]
    sexo = models.CharField(
        max_length=1,
        choices=opciones_sexo,
        default=femenino
    )
    fecha_nacimiento = models.DateTimeField()
    dpi = models.CharField(max_length=45, null=True, blank=True)
    nit = models.CharField(max_length=45, null=True, blank=True)
    es_socio = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='permisos'
    )
    objects = CustomUserManager()
    def __str__(self):
        return f'{self.first_name} {self.last_name} (id: {self.id})'