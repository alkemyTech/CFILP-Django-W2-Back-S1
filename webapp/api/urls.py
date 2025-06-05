from django.urls import path
from api.views import (ClienteListApiView,
                       ServicioListApiView, 
                       CoordinadorListAPIView,
                       EmpleadosListAPIView)

urlpatterns = [
    path('cliente/', ClienteListApiView.as_view()),
    path('coordinadores/', CoordinadorListAPIView.as_view()),
    path('empleados/', EmpleadosListAPIView.as_view()),
    #Servicios
    path('servicio/', ServicioListApiView.as_view()),
]
