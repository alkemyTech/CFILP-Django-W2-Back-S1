from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    fecha_servicio = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Reserva
        fields = ['fecha_servicio', 'cliente', 'servicio', 'empleado', 'coordinador']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'coordinador': forms.Select(attrs={'class': 'form-control'}),
        }
