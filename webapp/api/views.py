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
# endregion
