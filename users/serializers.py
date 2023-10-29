from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario  # Asegúrate de importar tu modelo de usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  # Reemplaza con el nombre de tu modelo de usuario
        fields = '__all__'  # Agrega los campos que quieras serializar
        extra_kwargs = {'password': {'write_only': True}}  # Para que la contraseña no se muestre al serializar

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  # Reemplaza con el nombre de tu modelo de usuario
        fields = '__all__'  # Agrega los campos necesarios para el registro
        extra_kwargs = {'password': {'write_only': True}}  # Para que la contraseña no se muestre al serializar
    def create(self, validated_data):
            # Utiliza make_password para cifrar la contraseña antes de guardarla
            validated_data['password'] = make_password(validated_data.get('password'))
            return super(RegistroSerializer, self).create(validated_data)