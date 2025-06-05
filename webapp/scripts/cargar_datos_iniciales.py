# cargar_datos_iniciales.py

from servicios.models import Servicio, Cliente, Empleado, Coordinador, Reserva
from django.utils import timezone

def run():
    # Cargar Servicios
    servicios_base = [
        "Salón de eventos",
        "Decoración para fiestas de 15 años",
        "Decoración para fiestas de casamientos",
        "Servicio de lunch",
        "Servicio de luz y sonido"
    ]

    for nombre in servicios_base:
        Servicio.objects.get_or_create(
            nombre=nombre,
            defaults={
                "descripcion": "Servicio creado automáticamente",
                "precio": 0,
                "activo": True
            }
        )

    # Cargar Clientes
    cliente1, _ = Cliente.objects.get_or_create(nombre="Ana", apellido="Gomez", defaults={"activo": True})
    cliente2, _ = Cliente.objects.get_or_create(nombre="Luis", apellido="Martinez", defaults={"activo": True})

    # Cargar Empleados
    empleado1, _ = Empleado.objects.get_or_create(nombre="Carlos", apellido="Perez", defaults={"numero_legajo": 101, "activo": True})
    empleado2, _ = Empleado.objects.get_or_create(nombre="Marta", apellido="Lopez", defaults={"numero_legajo": 102, "activo": True})

    # Cargar Coordinadores
    coordinador1, _ = Coordinador.objects.get_or_create(nombre="Jorge", apellido="Suarez", defaults={"numero_documento": 12345678, "activo": True})
    coordinador2, _ = Coordinador.objects.get_or_create(nombre="Lucía", apellido="Fernandez", defaults={"numero_documento": 87654321, "activo": True})

    # Cargar Reservas si hay servicios cargados
    servicios = Servicio.objects.filter(activo=True)[:2]

    if servicios.count() >= 2:
        Reserva.objects.get_or_create(
            cliente=cliente1,
            servicio=servicios[0],
            empleado=empleado1,
            coordinador=coordinador1,
            fecha_servicio=timezone.now() + timezone.timedelta(days=7)
        )

        Reserva.objects.get_or_create(
            cliente=cliente2,
            servicio=servicios[1],
            empleado=empleado2,
            coordinador=coordinador2,
            fecha_servicio=timezone.now() + timezone.timedelta(days=10)
        )
        
run()
