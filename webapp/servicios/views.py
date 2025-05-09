from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from .models import Servicio, Reserva

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
