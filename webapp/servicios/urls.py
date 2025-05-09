from django.urls import path
from .views import (
    ServicioListView,
    ServicioCreateView,
    ServicioUpdateView,
    ServicioDeactivateView,
    ServicioRestoreView,
    ReservaListView,
    ReservaCreateView,
    ReservaUpdateView,
    
)

urlpatterns = [
    
    # Servicio
    path('servicio/', ServicioListView.as_view(), name='servicio_list'),
    path('servicio/nuevo/', ServicioCreateView.as_view(), name='servicio_create'),
    path('servicio/<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_edit'),
    path('servicio/<int:pk>/desactivar/', ServicioDeactivateView.as_view(), name='servicio_desactivar'),
    path('servicio/<int:pk>/restaurar/', ServicioRestoreView.as_view(), name='servicio_restaurar'),
    
    # Reserva
    
    path('reserva/', ReservaListView.as_view(), name='reserva_list'),
    path('reserva/nuevo/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reserva/<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_edit'),
   
]