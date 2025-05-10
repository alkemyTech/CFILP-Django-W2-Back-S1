from django.contrib import admin
from .models import Servicio
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.admin import SimpleListFilter

from .models import Servicio, Empleado, Cliente, Coordinador, Reserva


class FiltroEstado(SimpleListFilter):
    """ Filtro personalizado para el panel de administración,  con etiquetas en español:
    - 'Activos'
    - 'Inactivos'

    Este filtro debe usarse en modelos que implementan baja lógica.
    Se integra fácilmente en 'list_filter' y mejora la legibilidad de la interfaz """
    
    title = 'Estado'
    parameter_name = 'activo'

    def lookups(self, request, model_admin):
        return (
            ('True', 'Activos'),
            ('False', 'Inactivos'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(activo=True)
        if self.value() == 'False':
            return queryset.filter(activo=False)
        return queryset


class BajaLogica(admin.ModelAdmin):
    """ Clase base para administrar cualquier modelo que tenga un campo 'activo'.
        Permite:
        - Mostrar solo objetos activos por defecto
        - Realizar baja lógica (no borrar realmente)
        - Restaurar objetos desde el admin
        - Usar una columna con botón de restaurar
        - Restaurar varios objetos al mismo tiempo (acción masiva) """

    list_filter = (FiltroEstado,)  # Filtro lateral
    actions = ["restaurar"]    # Acción masiva

    def get_urls(self):
        """ Agrega una url para restaurar obejeto"""
        
        urls = super().get_urls()
        modelo = self.model._meta.model_name
        urls_personalizadas = [
            path('restaurar/<int:obj_id>/', self.admin_site.admin_view(self.restaurar), name= f"{modelo}-restaurar"),]
        
        return urls_personalizadas + urls

    def restaurar(self, request, obj_id):
        """ Restaura un solo objeto (activo = True) desde el botón en la tabla """
        
        obj = self.model.objects.get(id=obj_id)
        obj.activo = True
        obj.save()
        self.message_user(request, f"{self.model.__name__} restaurado correctamente.", messages.SUCCESS)
        return redirect(request.META.get("HTTP_REFERER", "/admin/"))

    def delete_model(self, request, obj):
        """ Reemplaza la eliminación por una baja lógica """
        
        obj.activo = False
        obj.save()

    def has_delete_permission(self, request, obj=None):
        """ Muestra el botón "Eliminar """
        
        return True

    @admin.action(description="Restaurar seleccionados")
    def restaurar_seleccionados(self, request, queryset):
        """ Acción masiva para restaurar varios objetos al mismo tiempo """
        
        cantidad = queryset.update(activo=True)
        self.message_user(request, f"{cantidad} objeto(s) restaurado(s).")

    def acciones(self, obj):
        """ Agrega una columna con botón de eliminar si el objeto esta activo o restaurar si está inactivo """
        
    
        if obj.activo:
            return format_html('<a href="{}/delete/">Eliminar</a>', obj.id)
        else:
            return format_html('<a href="restaurar/{}/">Restaurar</a>', obj.id)
    acciones.short_description = "Acción"


@admin.register(Servicio)
class ServicioAdmin(BajaLogica):
    list_display = ("nombre", "precio", "activo", "acciones")
    search_fields = ("nombre",)


@admin.register(Cliente)
class ClienteAdmin(BajaLogica):
    list_display = ("nombre", "apellido", "activo", "acciones")
    search_fields = ("nombre", "apellido")


@admin.register(Empleado)
class EmpleadoAdmin(BajaLogica):
    list_display = ("nombre", "apellido", "numero_legajo", "activo", "acciones")
    search_fields = ("nombre", "apellido")


@admin.register(Coordinador)
class CoordinadorAdmin(BajaLogica):
    list_display =("nombre", "apellido", "numero_documento", "fecha_alta", "activo", "acciones")
    search_fields = ("nombre", "apellido")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "servicio", "fecha_servicio", "fecha_reserva", "coordinador")
    search_fields = ("cliente__nombre", "servicio__nombre")
    list_filter = ("fecha_servicio", "servicio")