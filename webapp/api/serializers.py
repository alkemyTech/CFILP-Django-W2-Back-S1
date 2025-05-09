from rest_framework import serializers
from servicios.models import Cliente, Coordinador

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