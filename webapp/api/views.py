from django.shortcuts import render
from servicios.models import Cliente, Servicio, Reserva
from api.serializers import ClienteSerializer, ServicioSerializer, ReservaSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)

#region ---- CRUD CLIENTE ----

class ClienteListApiView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all()

#endregion

# region ----- CRUD para Servicios
class ServicioListApiView(ListAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.filter(activo=True) 

class ServicioDetailApiView(RetrieveAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.filter(activo=True)

class ServicioCreateApiView(CreateAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.all()

class ServicioUpdateApiView(UpdateAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.filter(activo=True)

class ServicioDeleteApiView(DestroyAPIView):
    serializer_class = ServicioSerializer
    
    def get_queryset(self):
        return Servicio.objects.filter(activo=True)
    
    def perform_destroy(self, instance):
        # Baja lógica
        instance.activo = False
        instance.save()
        
# endregion
        
# region ------ CRUD para reservas
        
class ReservaListApiView(ListAPIView):
    serializer_class = ReservaSerializer
    
    def get_queryset(self):
        return Reserva.objects.all()

class ReservaDetailApiView(RetrieveAPIView):
    serializer_class = ReservaSerializer
    
    def get_queryset(self):
        return Reserva.objects.all()

class ReservaCreateApiView(CreateAPIView):
    serializer_class = ReservaSerializer
    
    def get_queryset(self):
        return Reserva.objects.all()
    
# endregion
