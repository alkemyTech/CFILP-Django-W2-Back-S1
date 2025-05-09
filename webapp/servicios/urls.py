from django.urls import path
from .views import (
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
    
)

urlpatterns = [
    #empleados
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('empleados/<int:pk>/desactivar/', EmpleadoDeactivateView.as_view(), name='empleado_desactivar'),
    path('empleados/<int:pk>/restaurar/', EmpleadoRestoreView.as_view(), name='empleado_restaurar'),
    #Opcional
    #path('empleados/inactivos/', EmpleadoInactivosListView.as_view(), name='empleado_inactivos'),
    
    #cliente
    path('clientes/list', ClienteListView.as_view(), name="cliente-list"),
    path('clientes/create', ClienteCreateView.as_view(), name="cliente-create"),
    path('clientes/update/<int:pk>', ClienteUpdateView.as_view(), name="cliente-update"),
    path('clientes/activo/<int:pk>', ClienteActivoView.as_view(), name="cliente-activo"),
]
