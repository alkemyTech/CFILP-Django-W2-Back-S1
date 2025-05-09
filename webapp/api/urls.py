from django.urls import path
from api.views import (ClienteListApiView,
                    ServicioListApiView,
                    ServicioDetailApiView,
                    ServicioCreateApiView,
                    ServicioUpdateApiView,
                    ServicioDeleteApiView,
                    ReservaListApiView,
                    ReservaDetailApiView,
                    ReservaCreateApiView,)

urlpatterns = [
    path('cliente/', ClienteListApiView.as_view()),
    
    #Servicios
    path('servicio/', ServicioListApiView.as_view()),
    path('servicio/create/', ServicioCreateApiView.as_view()),
    path('servicio/<int:pk>/', ServicioDetailApiView.as_view()),
    path('servicio/<int:pk>/update/', ServicioUpdateApiView.as_view()),
    path('servicio/<int:pk>/delete/', ServicioDeleteApiView.as_view()),
    
    #Reservas
    path('reserva/', ReservaListApiView.as_view()),
    path('reserva/<int:pk>/', ReservaDetailApiView.as_view()),
    path('reserva/create/', ReservaCreateApiView.as_view()),
]
