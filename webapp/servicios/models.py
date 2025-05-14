from django.db import models

# Creo el modelo Empleado que tiene los campos name, lastname, numero_legajo, active
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_legajo = models.IntegerField(null=True, blank=True, default=0)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Servicio(models.Model):
    
    """Representa los servicios ofrecidos por la empresa de eventos"""
    
    nombre = models.CharField(max_length=255, help_text="Nombre específico del servicio")
    descripcion = models.TextField(help_text="Descripción detallada del servicio")
    precio = models.FloatField(help_text="Precio del servicio")
    activo = models.BooleanField(default=True, help_text="Estado lógico del servicio (True = activo)")
    
    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['nombre']

class Coordinador(models.Model):
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100)
    numero_documento = models.IntegerField() 
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True) 

    def desactivar(self):
        self.activo = False
        self.save()
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reserva(models.Model):
    fecha_reserva = models.DateField(auto_now_add=True)
    fecha_servicio = models.DateTimeField(auto_now=False, auto_now_add=False)
    cliente = models.ForeignKey('servicios.Cliente', on_delete=models.CASCADE)
    servicio = models.ForeignKey('servicios.Servicio', on_delete=models.CASCADE)
    empleado = models.ForeignKey('servicios.Empleado', on_delete=models.CASCADE)
    coordinador = models.ForeignKey('servicios.Coordinador', on_delete=models.CASCADE)
