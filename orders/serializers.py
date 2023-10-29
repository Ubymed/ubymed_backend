from rest_framework import serializers
from .models import Orden, OrdenConsultaMedica, OrdenPruebaLaboratorio, DetalleOrdenLaboratorio

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'

class OrdenConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenConsultaMedica
        fields = '__all__'

class OrdenPruebaLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPruebaLaboratorio
        fields = '__all__'

class DetalleOrdenLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrdenLaboratorio
        fields = '__all__'