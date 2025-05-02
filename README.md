# WebApp

Esta es una aplicación web desarrollada en Python utilizando el framework Django, orientada a la gestión de reservas de servicios para eventos. Permite registrar y administrar servicios, clientes, empleados, coordinadores y las reservas realizadas.


## Contenido del Proyecto

1. **Modelos** Se han definido y modelado las siguientes entidades del sistema:
    -Coordinador
    -Cliente
    -Empleado
    -Servicio
    -Reserva

2. **Configuración del Admin** Todos los modelos están registrados y disponibles desde el panel de administración de Django (/admin). Desde allí se pueden:

    -Crear, editar y eliminar (lógicamente) registros.

    -Realizar búsquedas por nombre o apellido (según el modelo).

3. **Bajas Lógicas** Se ha implementado la funcionalidad de bajas lógicas para los siguientes modelos:
    
    -Coordinador

    -Cliente

    -Empleado

    -Servicio

Esto significa que al "eliminar" una instancia, su campo activo se marca como False, evitando su borrado físico. También se implementaron vistas para restaurar registros dados de baja.


## Cómo Usar la Aplicación

1. **Clonar el Repositorio**:
    ```bash
    git clone https://github.com/usuario/wepApp.git
    cd wepApp
    ```
2. **Activar un Entorono Virtual**:
    ```bash
    python -m venv venv
    venv\Scripts\activate 
    ```

3. **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Migrar la Base de Datos**:
    Aplica las migraciones para configurar la base de datos:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Crear un Superusuario**:
    Crea un superusuario para acceder al panel:
    ```bash
    python manage.py createsuperuser
    ```

6. **Ejecutar el Servidor**:
    Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. **Acceso al Admin**:
    Ve a `http://127.0.0.1:8000/admin` para gestionar los datos desde la interfaz de administración.


Desarrollado por Soraya Violini, Enzo Bonino, Gonzalo Fernandez y José Herrera.
