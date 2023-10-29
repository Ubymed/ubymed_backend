from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Orden, OrdenConsultaMedica, OrdenPruebaLaboratorio, DetalleOrdenLaboratorio
from .serializers import OrdenSerializer, OrdenConsultaMedicaSerializer, OrdenPruebaLaboratorioSerializer, DetalleOrdenLaboratorioSerializer

class OrdenAPIView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        usuario = request.query_params.get('usuario')
        estado = request.query_params.get('estado')
        ordenes = Orden.objects.all()
        if id:
            ordenes = ordenes.filter(id=id)
        if usuario:
            ordenes = ordenes.filter(usuario=usuario)
        if estado:
            ordenes = ordenes.filter(estado=estado)
        serializer = OrdenSerializer(ordenes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = OrdenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update_order(self, request, partial=False):
        id = request.data.get('id')
        if id:
            try:
                orden = Orden.objects.get(id=id)
            except Orden.DoesNotExist:
                return Response('La orden no existe', status=status.HTTP_404_NOT_FOUND)
            serializer = OrdenSerializer(orden, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('ID de orden no proporcionado', status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request):
        return self.update_order(request, partial=True)
    def put(self, request):
        return self.update_order(request, partial=False)
    
class OrdenCreateAPIView(CreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenConsultaMedicaAPIView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        orden_id = request.query_params.get('orden_id')
        ordenes = OrdenConsultaMedica.objects.all()
        if id:
            ordenes = ordenes.filter(id=id)
        if orden_id:
            ordenes = ordenes.filter(orden_id=orden_id)
        serializer = OrdenConsultaMedicaSerializer(ordenes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = OrdenConsultaMedicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update_order(self, request, partial=False):
        id = request.data.get('id')
        if id:
            try:
                orden = OrdenConsultaMedica.objects.get(id=id)
            except OrdenConsultaMedica.DoesNotExist:
                return Response('La orden de consulta médica no existe', status=status.HTTP_404_NOT_FOUND)
            serializer = OrdenConsultaMedicaSerializer(orden, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('ID de orden de consulta médica no proporcionado', status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request):
        return self.update_order(request, partial=True)
    def put(self, request):
        return self.update_order(request, partial=False)

class OrdenConsultaMedicaCreateAPIView(CreateAPIView):
    queryset = OrdenConsultaMedica.objects.all()
    serializer_class = OrdenConsultaMedicaSerializer

class OrdenConsultaMedicaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrdenConsultaMedica.objects.all()
    serializer_class = OrdenConsultaMedicaSerializer

class OrdenPruebaLaboratorioAPIView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        orden_id = request.query_params.get('orden_id')
        ordenes = OrdenPruebaLaboratorio.objects.all()
        if id:
            ordenes = ordenes.filter(id=id)
        if orden_id:
            ordenes = ordenes.filter(orden_id=orden_id)
        serializer = OrdenPruebaLaboratorioSerializer(ordenes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = OrdenPruebaLaboratorioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update_order(self, request, partial=False):
        id = request.data.get('id')
        if id:
            try:
                orden = OrdenPruebaLaboratorio.objects.get(id=id)
            except OrdenPruebaLaboratorio.DoesNotExist:
                return Response('La orden de laboratorios no existe', status=status.HTTP_404_NOT_FOUND)
            serializer = OrdenPruebaLaboratorioSerializer(orden, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('ID de orden de laboratorios no proporcionado', status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request):
        return self.update_order(request, partial=True)
    def put(self, request):
        return self.update_order(request, partial=False)
    
class OrdenLaboratorioCreateAPIView(CreateAPIView):
    queryset = OrdenPruebaLaboratorio.objects.all()
    serializer_class = OrdenPruebaLaboratorioSerializer

class OrdenLaboratoriosRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrdenPruebaLaboratorio.objects.all()
    serializer_class = OrdenPruebaLaboratorioSerializer

class DetalleOrdenLaboratorioAPIView(APIView):
    def get(self, request):
        orden_id = request.query_params.get('orden_id')
        ordenes = Orden.objects.all()
        if orden_id:
            ordenes = ordenes.filter(orden_id=orden_id)
        serializer = OrdenSerializer(ordenes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = DetalleOrdenLaboratorioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleOrdenLaboratorioCreateAPIView(CreateAPIView):
    queryset = DetalleOrdenLaboratorio.objects.all()
    serializer_class = DetalleOrdenLaboratorioSerializer

class DetalleOrdenLaboratorioRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DetalleOrdenLaboratorio.objects.all()
    serializer_class = DetalleOrdenLaboratorioSerializer