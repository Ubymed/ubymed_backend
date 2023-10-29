from rest_framework import generics
from .models import LaboratorioClinico, SedeLaboratorioClinico, Socio, Medico, Flebotomista
from .serializers import LaboratorioClinicoSerializer, SedeLaboratorioClinicoSerializer, SocioSerializer, MedicoSerializer, FlebotomistaSerializer

class SocioListAPIView(generics.ListAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

class SocioCreateAPIView(generics.CreateAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

class SocioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

class LaboratorioClinicoListAPIView(generics.ListAPIView):
    queryset = LaboratorioClinico.objects.all()
    serializer_class = LaboratorioClinicoSerializer

class LaboratorioClinicoCreateAPIView(generics.CreateAPIView):
    queryset = LaboratorioClinico.objects.all()
    serializer_class = LaboratorioClinicoSerializer

class LaboratorioClinicoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaboratorioClinico.objects.all()
    serializer_class = LaboratorioClinicoSerializer

class SedeLaboratorioClinicoListAPIView(generics.ListAPIView):
    queryset = SedeLaboratorioClinico.objects.all()
    serializer_class = SedeLaboratorioClinicoSerializer

class SedeLaboratorioClinicoCreateAPIView(generics.CreateAPIView):
    queryset = SedeLaboratorioClinico.objects.all()
    serializer_class = SedeLaboratorioClinicoSerializer

class SedeLaboratorioClinicoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaboratorioClinico.objects.all()
    serializer_class = LaboratorioClinicoSerializer

class MedicoListAPIView(generics.ListAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoCreateAPIView(generics.CreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class FlebotomistaListAPIView(generics.ListAPIView):
    queryset = Flebotomista.objects.all()
    serializer_class = FlebotomistaSerializer

class FlebotomistaCreateAPIView(generics.CreateAPIView):
    queryset = Flebotomista.objects.all()
    serializer_class = FlebotomistaSerializer

class FlebotomistaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flebotomista.objects.all()
    serializer_class = FlebotomistaSerializer