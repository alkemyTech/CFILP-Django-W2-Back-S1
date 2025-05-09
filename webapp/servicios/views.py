from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from .models import Coordinador

# Listado de coordinadores activos
class CoordinadorListView(ListView):
    model = Coordinador

    def get_queryset(self):
        return Coordinador.objects.filter(activo=True)

# Crear un nuevo coordinador
class CoordinadorCreateView(CreateView):
    model = Coordinador
    fields = ['nombre', 'apellido', 'numero_documento', 'activo']
    success_url = reverse_lazy('coordinador_list')

# Editar un coordinador existente
class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    fields = ['nombre', 'apellido', 'numero_documento', 'activo']
    success_url = reverse_lazy('coordinador_list')

# Baja lógica (desactivar)
class CoordinadorDeactivateView(View):
    def post(self, request, pk):
        coordinador = get_object_or_404(Coordinador, pk=pk)
        coordinador.activo = False
        coordinador.save()
        return redirect('coordinador_list')

# Restaurar coordinador inactivo
class CoordinadorRestoreView(View):
    def post(self, request, pk):
        coordinador = get_object_or_404(Coordinador, pk=pk)
        coordinador.activo = True
        coordinador.save()
        return redirect('coordinador_inactivos')

class CoordinadorInactivosListView(ListView):
    model = Coordinador

    def get_queryset(self):
        return Coordinador.objects.filter(activo=False)
