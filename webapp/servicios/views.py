from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Cliente

# READ
class ClienteListView(ListView):
    model = Cliente
    template_name = 'servicios/cliente-list.html'
    query_set = Cliente.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'servicios/cliente-create.html'
    fields = ['nombre', 'apellido', 'activo']
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'activo']
    template_name = 'servicios/cliente-update.html'
    success_url = reverse_lazy('cliente-list')

class ClienteActivoView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        if cliente.activo == True:
            cliente.activo = False
        else: cliente.activo = True
        cliente.save()
        return redirect('cliente-list')
