from rest_framework import serializers
from .models import Servicio, ConsultaMedica, PruebaLaboratorio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'

class PruebaLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaLaboratorio
        fields = '__all__'