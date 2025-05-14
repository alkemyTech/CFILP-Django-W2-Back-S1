from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from .models import (Empleado, Cliente, Servicio, Reserva, Coordinador)

# View
class HomeView(TemplateView):   
    template_name = 'home.html'
    
#####   QUITAR O COMENTAR PARA PROBAR EL HOME ######    
# Servicio
class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicio/servicio_list.html'
    def get_queryset(self):
        return Servicio.objects.filter(activo=True)

class ServicioCreateView(CreateView):
    model =Servicio
    fields = '__all__'
    template_name = 'servicio/servicio_form.html' 
    success_url = reverse_lazy('servicio_list')

class ServicioUpdateView(UpdateView):
    model =Servicio
    fields = '__all__'
    template_name = 'servicio/servicio_form.html' 
    success_url = reverse_lazy('servicio_list')

class ServicioDeactivateView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk) 
        servicio.activo = False
        servicio.save()
        return redirect('servicio_list')

class ServicioRestoreView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.activo = True
        servicio.save()
        return redirect('servicio_inactivos')
# ---------
# Reserva 
class ReservaListView(ListView):
    model = Servicio
    template_name = 'reserva/reserva_list.html'
    def get_queryset(self):
        return Servicio.objects.filter(activo=True)

class ReservaCreateView(CreateView):
    model =Servicio
    fields = '__all__'
    template_name = 'reserva/reserva_form.html' 
    success_url = reverse_lazy('reserva_list')

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = '__all__'
    template_name = 'reserva/reserva_form.html' 
    success_url = reverse_lazy('reserva_list')

class ReservaDeleteView(DeleteView):
    model = Reserva
    fields = '__all__'
    template_name = 'reserva/reserva_form.html'
    success_url = reverse_lazy('reserva_list')
# --------
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
    template_name = 'empleados/empleado_form.html' # Formulario
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

# READ clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'servicios/cliente-list.html'
    query_set = Cliente.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# CREATE clientes
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'servicios/cliente-create.html'
    fields = ['nombre', 'apellido', 'activo']
    success_url = reverse_lazy('cliente-list')

# UPDATE clientes
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'activo']
    template_name = 'servicios/cliente-update.html'
    success_url = reverse_lazy('cliente-list')

# DELETE clientes
class ClienteActivoView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        if cliente.activo == True:
            cliente.activo = False
        else: cliente.activo = True
        cliente.save()
        return redirect('cliente-list')

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

