from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    IndexView,
    ContactoCreateView,
    )


urlpatterns = [


    # Home
    path('home/', HomeView.as_view(), name='home'),
    path('', ContactoCreateView.as_view(), name='index'),
    
    # Mensaje de contacto
    path('', ContactoCreateView.as_view(), name='contacto'),  
  
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
    path('reserva/<int:pk>/eliminar/', ReservaDeleteView.as_view(), name='reserva_delete'),

    #empleados
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('empleados/<int:pk>/desactivar/', EmpleadoDeactivateView.as_view(), name='empleado_desactivar'),
    path('empleados/<int:pk>/restaurar/', EmpleadoRestoreView.as_view(), name='empleado_restaurar'),
    #Opcional
    #path('empleados/inactivos/', EmpleadoInactivosListView.as_view(), name='empleado_inactivos'),
    
    #cliente
  
    path('cliente/', ClienteListView.as_view(), name="cliente_list"),
    path('cliente/create', ClienteCreateView.as_view(), name="cliente_create"),
    path('cliente/<int:pk>/update/', ClienteUpdateView.as_view(), name="cliente_update"),
    path('cliente/<int:pk>/activo/', ClienteActivoView.as_view(), name="cliente_activo"),
  
    #coordinador

    path('coordinadores/', CoordinadorListView.as_view(), name='coordinador_list'),
    path('coordinadores/nuevo/', CoordinadorCreateView.as_view(), name='coordinador_create'),
    path('coordinadores/<int:pk>/editar/', CoordinadorUpdateView.as_view(), name='coordinador_edit'),
    path('coordinadores/<int:pk>/desactivar/', CoordinadorDeactivateView.as_view(), name='coordinador_desactivar'),
    path('coordinadores/<int:pk>/restaurar/', CoordinadorRestoreView.as_view(), name='coordinador_restaurar'),
    path('coordinadores/inactivos/', CoordinadorInactivosListView.as_view(), name='coordinador_inactivos'),    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
