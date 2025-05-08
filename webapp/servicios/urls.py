from django.urls import path
from .views import (
    EmpleadoListView,
    EmpleadoCreateView,
    EmpleadoUpdateView,
    EmpleadoDeactivateView,
    EmpleadoRestoreView,
    #EmpleadoInactivosListView
    
    
)

urlpatterns = [
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('empleados/<int:pk>/desactivar/', EmpleadoDeactivateView.as_view(), name='empleado_desactivar'),
    path('empleados/<int:pk>/restaurar/', EmpleadoRestoreView.as_view(), name='empleado_restaurar'),
    #Opcional
    #path('empleados/inactivos/', EmpleadoInactivosListView.as_view(), name='empleado_inactivos'),

]