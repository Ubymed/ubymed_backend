from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario  # Asegúrate de importar tu modelo de usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'telefono', 'sexo', 'fecha_nacimiento', 'dpi', 'nit', 'es_socio')

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario