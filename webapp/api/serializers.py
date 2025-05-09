from rest_framework import serializers
from servicios.models import Cliente, Servicio, Reserva, Coordinador


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nombre',
            'apellido',
            'activo'
        ]
        

class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Servicio.
    Convierte instancias a JSON y valida entradas."""
    
    class Meta:
        model = Servicio
        fields = '__all__'
        
class ReservaSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Validación de integridad. Las reservan se asocian sólo con activos
        entidades = ['servicio']
        for campo in entidades:
            if not data[campo].activo:
                raise serializers.ValidationError(f"{campo.capitalize()} inactivo.")
        return data

    class Meta:
        model = Reserva
        fields = '__all__'

