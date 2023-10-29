"""
URL configuration for ubymed_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import RegistroAPIView, LoginAPIView, LogoutAPIView, UsuarioRetrieveUpdateAPIView
from services.views import ServicioListAPIView, ConsultaMedicaListAPIView, PruebaLaboratorioListAPIView, ServicioCreateAPIView, ServicioRetrieveUpdateDestroyAPIView, ConsultaMedicaCreateAPIView, ConsultaMedicaRetrieveUpdateDestroyAPIView, PruebaLaboratorioCreateAPIView, PruebaLaboratorioRetrieveUpdateDestroyAPIView
from orders.views import OrdenAPIView, OrdenConsultaMedicaAPIView, OrdenPruebaLaboratorioAPIView, DetalleOrdenLaboratorioAPIView, OrdenRetrieveUpdateDestroyAPIView, OrdenConsultaMedicaRetrieveUpdateDestroyAPIView, OrdenLaboratoriosRetrieveUpdateDestroyAPIView, DetalleOrdenLaboratorioRetrieveUpdateDestroyAPIView
from partners.views import SocioCreateAPIView, SocioRetrieveUpdateDestroyAPIView, SocioListAPIView, MedicoListAPIView, MedicoCreateAPIView, MedicoRetrieveUpdateDestroyAPIView, FlebotomistaListAPIView, FlebotomistaCreateAPIView, FlebotomistaRetrieveUpdateDestroyAPIView, LaboratorioClinicoListAPIView, LaboratorioClinicoCreateAPIView, LaboratorioClinicoRetrieveUpdateDestroyAPIView, SedeLaboratorioClinicoListAPIView, SedeLaboratorioClinicoCreateAPIView, SedeLaboratorioClinicoRetrieveUpdateDestroyAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Ubymed API",
        default_version='v2.0',
        description="Ubymed API",
        terms_of_service="https://www.ubymed.com/",
        contact=openapi.Contact(email="mflores@ubymed.com"),
        license=openapi.License(name="Tu Licencia"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('usuarios/registro/', RegistroAPIView.as_view(), name='registro'),
    path('usuarios/login/', LoginAPIView.as_view(), name='login'),
    path('usuarios/logout/', LogoutAPIView.as_view(), name='logout'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateAPIView.as_view(), name='usuario'),
    path('socios/', SocioListAPIView.as_view(), name='socios'),
    path('socios/nuevo/', SocioCreateAPIView.as_view(), name='socio-nuevo'),
    path('socios/<int:pk>/', SocioRetrieveUpdateDestroyAPIView.as_view(), name='socio'),
    path('socios/laboratorios/', LaboratorioClinicoListAPIView.as_view(), name='laboratorios'),
    path('socios/laboratorios/<int:pk>/', LaboratorioClinicoListAPIView.as_view(), name='laboratorio'),
    path('socios/laboratorios-sedes/', SedeLaboratorioClinicoListAPIView.as_view(), name='laboratorios-sedes'),
    path('socios/laboratorios-sedes/<int:pk>', SedeLaboratorioClinicoRetrieveUpdateDestroyAPIView.as_view(), name='laboratorio-sede'),
    path('socios/medicos/', MedicoListAPIView.as_view(), name='medicos'),
    path('socios/medicos/nuevo/', MedicoCreateAPIView.as_view(), name='medico-nuevo'),
    path('socios/medicos/<int:pk>/', MedicoRetrieveUpdateDestroyAPIView.as_view(), name='medico'),
    path('socios/flebotomistas/', FlebotomistaListAPIView.as_view(), name='flebotomistas'),
    path('socios/flebotomistas/nuevo/', FlebotomistaListAPIView.as_view(), name='flebotomistas-nuevo'),
    path('socios/flebotomistas/<int:pk>/', FlebotomistaRetrieveUpdateDestroyAPIView.as_view(), name='flebotomista'),
    path('servicios/', ServicioListAPIView.as_view(), name='servicios'),
    path('servicios/consultas/', ConsultaMedicaListAPIView.as_view(), name='servicios-consultas'),
    path('servicios/laboratorios/', PruebaLaboratorioListAPIView.as_view(), name='servicios-laboratorios'),
    path('ordenes/', OrdenAPIView.as_view(), name='ordenes'),
    path('ordenes/<int:pk>/', OrdenRetrieveUpdateDestroyAPIView.as_view(), name='orden'),
    path('ordenes/consultas/', OrdenConsultaMedicaAPIView.as_view(), name='ordenes-consultas'),
    path('ordenes/consultas/<int:pk>/', OrdenConsultaMedicaRetrieveUpdateDestroyAPIView.as_view(), name='orden-consulta'),
    path('ordenes/laboratorios/', OrdenPruebaLaboratorioAPIView.as_view(), name='ordenes-laboratorios'),
    path('ordenes/laboratorios/<int:pk>/', OrdenLaboratoriosRetrieveUpdateDestroyAPIView.as_view(), name='orden-laboratorio'),
    path('ordenes/laboratorios/detalle/', DetalleOrdenLaboratorioAPIView.as_view(), name='ordenes-laboratorios-detalle'),
    path('ordenes/laboratorios/detalle/<int:pk>/', DetalleOrdenLaboratorioRetrieveUpdateDestroyAPIView.as_view(), name='orden-laboratorio-detalle'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
