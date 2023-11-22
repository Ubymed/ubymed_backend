from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}  # Para que la contraseña no se muestre al serializar
    def create(self, validated_data):
            # Utiliza make_password para cifrar la contraseña antes de guardarla
            validated_data['password'] = make_password(validated_data.get('password'))
            return super(RegistroSerializer, self).create(validated_data)