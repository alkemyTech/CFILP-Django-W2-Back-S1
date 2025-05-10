from django.shortcuts import render
<<<<<<< HEAD
from servicios.models import Cliente, Servicio, Reserva, Coordinador, Empleado
from api.serializers import ClienteSerializer, ServicioSerializer, ReservaSerializer, CoordinadorSerializer, EmpleadosSerializer
=======
from servicios.models import Cliente, Servicio, Reserva, Coordinador
from api.serializers import ClienteSerializer, ServicioSerializer, ReservaSerializer, CoordinadorSerializer
>>>>>>> 254ec8a1e2c99c64aabfaa4cd764c9bdce550ac9
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework import generics

#region ---- CLIENTE ----

class ClienteListApiView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(activo = True)

#endregion

#---- COORDINADOR ----
class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.filter(activo=True)
    serializer_class = CoordinadorSerializer

class CoordinadorDetailAPIView(generics.RetrieveAPIView):
   queryset = Coordinador.objects.filter(activo=True)
   serializer_class = CoordinadorSerializer
  
# region ----- Servicios
class ServicioListApiView(ListAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.filter(activo=True) 
# endregion

# ---- Empleados
class EmpleadosListAPIView(ListAPIView):
    serializer_class = EmpleadosSerializer
    
    def get_queryset(self):
        return Empleado.objects.filter(activo=True) 
# endregion
