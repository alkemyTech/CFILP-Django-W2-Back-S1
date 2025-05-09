from django.urls import path
from servicios.views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteActivoView

urlpatterns = [
    path('clientes/list', ClienteListView.as_view(), name="cliente-list"),
    path('clientes/create', ClienteCreateView.as_view(), name="cliente-create"),
    path('clientes/update/<int:pk>', ClienteUpdateView.as_view(), name="cliente-update"),
    path('clientes/activo/<int:pk>', ClienteActivoView.as_view(), name="cliente-activo"),
    ]