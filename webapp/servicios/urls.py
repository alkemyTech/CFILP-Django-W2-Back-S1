from django.urls import path
from .views import HomeView
from .views import (                         #QUITAR O COMENTAR PARA PROBAR EL HOME
    ServicioListView,
    ServicioCreateView,
    ServicioUpdateView,
    ServicioDeactivateView,
    ServicioRestoreView,
    ReservaListView,
    ReservaCreateView,
    ReservaUpdateView,
    ReservaDeleteView,
    EmpleadoListView,
    EmpleadoCreateView,
    EmpleadoUpdateView,
    EmpleadoDeactivateView,
    EmpleadoRestoreView,
    #EmpleadoInactivosListView,
    ClienteListView, 
    ClienteCreateView,
    ClienteUpdateView,
    ClienteActivoView, 
    CoordinadorListView,
    CoordinadorCreateView,
    CoordinadorUpdateView,
    CoordinadorDeactivateView,
    CoordinadorRestoreView,
    CoordinadorInactivosListView,
    HomeView, 
    )


urlpatterns = [
    
    # Home
    path('', HomeView.as_view(), name='home'),
  
    # Servicio
    #path('servicio/', ServicioListView.as_view(), name='servicio_list'),
    #path('servicio/nuevo/', ServicioCreateView.as_view(), name='servicio_create'),
    #path('servicio/<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_edit'),
    #path('servicio/<int:pk>/desactivar/', ServicioDeactivateView.as_view(), name='servicio_desactivar'),
    #path('servicio/<int:pk>/restaurar/', ServicioRestoreView.as_view(), name='servicio_restaurar'),
    
    # Reserva
    
    #path('reserva/', ReservaListView.as_view(), name='reserva_list'),
    #path('reserva/nuevo/', ReservaCreateView.as_view(), name='reserva_create'),
    #path('reserva/<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_edit'),
    #path('reserva/<int:pk>/eliminar/', ReservaDeleteView.as_view(), name='reserva_delete'),

    #empleados
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('empleados/<int:pk>/desactivar/', EmpleadoDeactivateView.as_view(), name='empleado_desactivar'),
    path('empleados/<int:pk>/restaurar/', EmpleadoRestoreView.as_view(), name='empleado_restaurar'),
    #Opcional
    #path('empleados/inactivos/', EmpleadoInactivosListView.as_view(), name='empleado_inactivos'),
    
    #cliente
    #path('clientes/list', ClienteListView.as_view(), name="cliente-list"),
    #path('clientes/create', ClienteCreateView.as_view(), name="cliente-create"),
    #path('clientes/update/<int:pk>', ClienteUpdateView.as_view(), name="cliente-update"),
    #path('clientes/activo/<int:pk>', ClienteActivoView.as_view(), name="cliente-activo"),
  
    #coordinador
    path('coordinadores/', CoordinadorListView.as_view(), name='coordinador_list'),
    path('coordinadores/nuevo/', CoordinadorCreateView.as_view(), name='coordinador_create'),
    path('coordinadores/<int:pk>/editar/', CoordinadorUpdateView.as_view(), name='coordinador_edit'),
    path('coordinadores/<int:pk>/desactivar/', CoordinadorDeactivateView.as_view(), name='coordinador_desactivar'),
    path('coordinadores/<int:pk>/restaurar/', CoordinadorRestoreView.as_view(), name='coordinador_restaurar'),
    path('coordinadores/inactivos/', CoordinadorInactivosListView.as_view(), name='coordinador_inactivos'),    
    
]
