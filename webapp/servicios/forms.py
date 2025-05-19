from django import forms
from .models import Reserva, Empleado, Coordinador, Cliente, Servicio

class ReservaForm(forms.ModelForm):
    fecha_servicio = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    # describe los campos para filtrar solo los activos
    cliente = forms.ModelChoiceField(
        #filtramos que muestre solo los activos
        queryset=Cliente.objects.filter(activo=True),
        #se le agregan los atributos a este elemento
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter(activo=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.filter(activo=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    coordinador = forms.ModelChoiceField(
        queryset=Coordinador.objects.filter(activo=True),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Reserva
        fields = ['fecha_servicio', 'cliente', 'servicio', 'empleado', 'coordinador']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'numero_legajo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_legajo': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CoordinadorForm(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = ['nombre', 'apellido','numero_documento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion','precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }
