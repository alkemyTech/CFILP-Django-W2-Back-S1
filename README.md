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

## API REST

La aplicación expone una API REST completa para consumir los modelos desde frontend, apps móviles o clientes externos. Todos los endpoints se encuentran bajo el prefijo `/api/`.

### Endpoints de la API REST

| Método | Endpoint                          | Descripción                           |
|--------|-----------------------------------|---------------------------------------|
| GET    | /api/servicios/                   | Listar servicios activos              |
| GET    | /api/servicios/<id>/              | Ver detalle de un servicio            |
| POST   | /api/servicios/create/            | Crear un nuevo servicio               |
| PUT    | /api/servicios/<id>/update/       | Actualizar un servicio                |
| DELETE | /api/servicios/<id>/delete/       | Baja lógica de un servicio            |

| GET    | /api/clientes/                    | Listar clientes activos               |
| GET    | /api/clientes/<id>/               | Ver detalle de un cliente             |
| POST   | /api/clientes/create/             | Crear un nuevo cliente                |
| PUT    | /api/clientes/<id>/update/        | Actualizar un cliente                 |
| DELETE | /api/clientes/<id>/delete/        | Baja lógica de un cliente             |

| GET    | /api/empleados/                   | Listar empleados activos              |
| GET    | /api/empleados/<id>/              | Ver detalle de un empleado            |
| POST   | /api/empleados/create/            | Crear un nuevo empleado               |
| PUT    | /api/empleados/<id>/update/       | Actualizar un empleado                |
| DELETE | /api/empleados/<id>/delete/       | Baja lógica de un empleado            |

| GET    | /api/coordinadores/               | Listar coordinadores activos          |
| GET    | /api/coordinadores/<id>/          | Ver detalle de un coordinador         |
| POST   | /api/coordinadores/create/        | Crear un nuevo coordinador            |
| PUT    | /api/coordinadores/<id>/update/   | Actualizar un coordinador             |
| DELETE | /api/coordinadores/<id>/delete/   | Baja lógica de un coordinador         |

| GET    | /api/reserva/                     | Listar todas las reservas             |
| GET    | /api/reserva/<id>/                | Ver detalle de una reserva            |
| POST   | /api/reserva/create/              | Crear una nueva reserva               |


Todas las relaciones dentro de `Reserva` validan que la entidad esté activa.

## Requisitos del sistema

- Python 3.10 o superior
- Django 5.x
- pip
- Sistema operativo compatible (Linux, Windows o macOS)


## Cómo Usar la Aplicación

1. **Clonar el Repositorio**:
    ```bash
    git clone https://github.com/alkemyTech/CFILP-Django-W2-Back-S1.git
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

## Carga de servicios base

Para crear automáticamente los servicios iniciales, ejecutá el siguiente script desde la raíz del proyecto:

```bash
python manage.py shell
>>> from scripts.cargar_datos_iniciales import run           
>>> run()
```



Desarrollado por Soraya Violini, Enzo Bonino, Gonzalo Fernandez y José Herrera.
