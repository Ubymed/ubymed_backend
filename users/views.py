from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import RegistroSerializer, UsuarioSerializer
from .permissions import ProprietorshipPermission

class RegistroAPIView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Iniciar sesión después del registro
            return Response(UsuarioSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response("Credenciales no válidas", status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()  # Revoca el Token
            return Response("Sesión cerrada con éxito", status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response("No se encontró un Token para este usuario", status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, ProprietorshipPermission]