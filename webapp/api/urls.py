from django.urls import path
from api.views import (ClienteListApiView,
                       ServicioListApiView, 
                       CoordinadorListAPIView, 
                       CoordinadorDetailAPIView,
                       EmpleadosListAPIView)

urlpatterns = [
    path('cliente/', ClienteListApiView.as_view()),
    path('empleados/', EmpleadosListAPIView.as_view()),
    path('coordinadores/', CoordinadorListAPIView.as_view(), name='api_coordinadores'),
    path('coordinadores/<int:pk>/', CoordinadorDetailAPIView.as_view(), name='api_coordinador_detalle'),
    #Servicios
    path('servicio/', ServicioListApiView.as_view()),
]
