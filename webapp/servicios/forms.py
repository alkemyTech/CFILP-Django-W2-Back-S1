from django import forms
from .models import Reserva, Cliente, Servicio, Empleado, Coordinador

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_servicio', 'cliente', 'servicio', 'empleado', 'coordinador']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(activo=True)
        self.fields['servicio'].queryset = Servicio.objects.filter(activo=True)
        self.fields['empleado'].queryset = Empleado.objects.filter(activo=True)
        self.fields['coordinador'].queryset = Coordinador.objects.filter(activo=True)
