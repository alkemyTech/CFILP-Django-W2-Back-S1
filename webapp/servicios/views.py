from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from .models import (Empleado, Cliente, Servicio, Reserva, Coordinador)
from .forms import EmpleadoForm, CoordinadorForm, ReservaForm


# View
class HomeView(TemplateView):   
    template_name = 'home.html'
    
    
#####   QUITAR O COMENTAR PARA PROBAR EL HOME ######    

#region --------- SERVICIOS --------- 

# READ
class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicio/servicio_list.html'

    def get_queryset(self):
        return Servicio.objects.filter(activo=True)

# CREATE
class ServicioCreateView(CreateView):
    model =Servicio
    fields = '__all__'
    template_name = 'servicio/servicio_form.html' 
    success_url = reverse_lazy('servicio_list')

#UPDATE
class ServicioUpdateView(UpdateView):
    model =Servicio
    fields = '__all__'
    template_name = 'servicio/servicio_form.html' 
    success_url = reverse_lazy('servicio_list')

#DELETE
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
        return redirect('servicio_list')
#endregion

#region --------- RESERVA ---------

class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva/reserva_list.html'
    def get_queryset(self):
        return Reserva.objects.all()

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reserva/reserva_form.html' 
    success_url = reverse_lazy('reserva_list') 

class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm 
    template_name = 'reserva/reserva_update.html' 
    success_url = reverse_lazy('reserva_list')

class ReservaDeleteView(DeleteView):
    model = Reserva
    fields = '__all__'
    template_name = 'reserva/reserva_form.html'
    success_url = reverse_lazy('reserva_list')
#endregion

#region --------- EMPlEADOS ---------

#Listar de empleados
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        return Empleado.objects.filter(activo=True) #muestro solos los que esten activos

#Crear empleados
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html' # Formulario
    success_url = reverse_lazy('empleado_list')
    form_class = EmpleadoForm

#Editar empleados
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
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
#endregion

#region --------- CLIENTES ---------

# READ clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    
    def get_queryset(self):
        return Cliente.objects.filter(activo=True)

# CREATE clientes
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente/cliente_form.html'
    fields = ['nombre', 'apellido', 'activo']
    success_url = reverse_lazy('cliente_list')

# UPDATE clientes
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'activo']
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

# DELETE clientes
class ClienteActivoView(View):
    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        if cliente.activo == True:
            cliente.activo = False
        else: cliente.activo = True
        cliente.save()
        return redirect('cliente_list')
#endregion

#region --------- COORDINADORES ---------

# Listado de coordinadores activos
class CoordinadorListView(ListView):
    model = Coordinador
    template_name = 'coordinadores/coordinador_list.html'
    context_object_name = 'coordinadores'

    def get_queryset(self):
        return Coordinador.objects.filter(activo=True)

# Crear un nuevo coordinador
class CoordinadorCreateView(CreateView):
    model = Coordinador
    success_url = reverse_lazy('coordinador_list')
    form_class = CoordinadorForm
    template_name = 'coordinadores/coordinador_form.html'

# Editar un coordinador existente
class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    form_class = CoordinadorForm
    template_name = 'coordinadores/coordinador_form.html'
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

#endregion

