from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from .models import Empleado

#Listar de empleados
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'

    def get_queryset(self):
        return Empleado.objects.filter(activo=True) #muestro solos los que esten activos
    
#Crear empleados
class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'numero_legajo', 'activo']
    template_name = 'empleados/empleado_form.html'  # Formulario
    success_url = reverse_lazy('empleado_list')

#Editar empleados
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'numero_legajo', 'activo']
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado_list')
    
    
class EmpleadoDeactivateView(View):
    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk) 
        empleado.activo = False
        empleado.save()
        return redirect('empleado_list')

class EmpleadoRestoreView(View):
    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.activo = True
        empleado.save()
        return redirect('empleado_inactivos')

#Opcional
'''
class EmpleadoInactivosListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_inactivos.html'

    def get_queryset(self):
        return Empleado.objects.filter(activo=False)
'''