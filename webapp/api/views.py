from django.shortcuts import render
from servicios.models import Cliente
from api.serializers import ClienteSerializer

from rest_framework.generics import (ListAPIView,)

#region ---- CLIENTE ----

class ClienteListApiView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(activo = True)

#endregion