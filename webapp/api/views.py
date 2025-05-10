from django.shortcuts import render
from servicios.models import Cliente, Servicio, Reserva, Coordinador
from api.serializers import ClienteSerializer, ServicioSerializer, ReservaSerializer, CoordinadorSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework import generics

#region ---- CLIENTE ----

class ClienteListApiView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(activo = True)

#endregion

#region---- COORDINADOR ----
class CoordinadorListAPIView(generics.ListAPIView):
    serializer_class = CoordinadorSerializer

    def get_queryset(self):
        return Coordinador.objects.filter(activo=True)
    
#endregion

# region ----- Servicios
class ServicioListApiView(ListAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.filter(activo=True) 
# endregion

