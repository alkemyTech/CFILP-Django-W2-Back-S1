from django.shortcuts import render
from servicios.models import Cliente , Coordinador
from rest_framework import generics
from api.serializers import ClienteSerializer
from .serializers import CoordinadorSerializer
from rest_framework.generics import (ListAPIView)

#region ---- CRUD CLIENTE ----

class ClienteListApiView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all()

#endregion

#---- CRUD COORDINADOR ----
class CoordinadorListAPIView(generics.ListAPIView):
    queryset = Coordinador.objects.filter(activo=True)
    serializer_class = CoordinadorSerializer

class CoordinadorDetailAPIView(generics.RetrieveAPIView):
   queryset = Coordinador.objects.filter(activo=True)
   serializer_class = CoordinadorSerializer