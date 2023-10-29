from rest_framework import generics
from .models import Servicio, ConsultaMedica, PruebaLaboratorio
from .serializers import ServicioSerializer, ConsultaMedicaSerializer, PruebaLaboratorioSerializer

class ServicioListAPIView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioCreateAPIView(generics.CreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ConsultaMedicaListAPIView(generics.ListAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class ConsultaMedicaCreateAPIView(generics.CreateAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class ConsultaMedicaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class PruebaLaboratorioListAPIView(generics.ListAPIView):
    serializer_class = PruebaLaboratorioSerializer
    def get_queryset(self):
        laboratorio_id = self.request.query_params.get('laboratorio_id', None)
        if laboratorio_id:
            return PruebaLaboratorio.objects.filter(laboratorio_id=laboratorio_id)
        else:
            return PruebaLaboratorio.objects.all()

class PruebaLaboratorioCreateAPIView(generics.CreateAPIView):
    queryset = PruebaLaboratorio.objects.all()
    serializer_class = PruebaLaboratorioSerializer

class PruebaLaboratorioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PruebaLaboratorio.objects.all()
    serializer_class = PruebaLaboratorioSerializer