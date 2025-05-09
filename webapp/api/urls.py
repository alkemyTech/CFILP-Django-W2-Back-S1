from django.urls import path
from api.views import (ClienteListApiView,
                    ServicioListApiView,)

urlpatterns = [
    path('cliente/', ClienteListApiView.as_view()),
    
    #Servicios
    path('servicio/', ServicioListApiView.as_view()),
]
