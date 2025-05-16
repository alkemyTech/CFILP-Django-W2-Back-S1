from django.shortcuts import render
from servicios.models import Cliente, Servicio, Reserva, Coordinador, Empleado
from api.serializers import ClienteSerializer, ServicioSerializer, ReservaSerializer, CoordinadorSerializer, EmpleadosSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework import generics

#region ---- CLIENTE ----

class ClienteListApiView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(activo = True)

#endregion

#region ---- COORDINADOR ----

class CoordinadorListAPIView(generics.ListAPIView):
    serializer_class = CoordinadorSerializer
    
    def get_queryset(self):
        return Coordinador.objects.filter(activo=True)

class CoordinadorDetailAPIView(generics.RetrieveAPIView):
   queryset = Coordinador.objects.filter(activo=True)
   serializer_class = CoordinadorSerializer
# endregion
  
# region ---- Servicios ----

class ServicioListApiView(ListAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.filter(activo=True) 
# endregion

# region ---- Empleados ----
class EmpleadosListAPIView(ListAPIView):
    serializer_class = EmpleadosSerializer
    
    def get_queryset(self):
        return Empleado.objects.filter(activo=True) 
# endregion
