from django.urls import path
from .views import CoordinadorListView, CoordinadorCreateView, CoordinadorUpdateView, CoordinadorDeactivateView, CoordinadorRestoreView, CoordinadorInactivosListView

urlpatterns = [
    path('coordinadores/', CoordinadorListView.as_view(), name='empleado_list'),
    path('coordinadores/nuevo/', CoordinadorCreateView.as_view(), name='empleado_create'),
    path('coordinadores/<int:pk>/editar/', CoordinadorUpdateView.as_view(), name='empleado_edit'),
    path('coordinadores/<int:pk>/desactivar/', CoordinadorDeactivateView.as_view(), name='empleado_desactivar'),
    path('coordinadores/<int:pk>/restaurar/', CoordinadorRestoreView.as_view(), name='empleado_restaurar'),
    path('coordinadores/inactivos/', CoordinadorInactivosListView.as_view(), name='empleado_inactivos'),    
]
