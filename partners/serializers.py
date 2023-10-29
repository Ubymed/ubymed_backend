from rest_framework import serializers
from .models import LaboratorioClinico, SedeLaboratorioClinico, Socio, Medico, Flebotomista

class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class LaboratorioClinicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratorioClinico
        fields = '__all__'

class SedeLaboratorioClinicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedeLaboratorioClinico
        fields = '__all__'

class FlebotomistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flebotomista
        fields = '__all__'