from django.urls import path
from api.views import (ClienteListApiView,
                       ServicioListApiView, 
                       CoordinadorListAPIView, 
                       )

urlpatterns = [
    path('cliente/', ClienteListApiView.as_view()),
    path('coordinadores/', CoordinadorListAPIView.as_view(), name='api_coordinadores'),
    #Servicios
    path('servicio/', ServicioListApiView.as_view()),
]
