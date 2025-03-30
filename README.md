## 📑 Índice

- [🛠️ Proyecto SMA - Registro y Reporte PPDA CQP](#proyecto-sma---registro-y-reporte-ppda-cqp)
- [🗂️ Estructura de Archivos del Proyecto](#estructura-de-archivos-del-proyecto)
- [🗄️ Estructura de Base de Datos (PostgreSQL - Supabase)](#estructura-de-base-de-datos-postgresql---supabase)
- [🧩 Estructura de modelos Django](#estructura-de-modelos-django)
- [🌐 Endpoints REST disponibles](#endpoints-rest-disponibles)
- [🔍 Funcionalidad de los endpoints](#funcionalidad-de-los-endpoints)
- [📄 Documentación de la API](#documentación-de-la-api)
- [📊 Estructura relacional de la base de datos](#estructura-relacional-de-la-base-de-datos)

## 🗂️ Estructura de archivos del proyecto

```
M5 - 3 - APP SMA/                # Carpeta raíz del proyecto

├── env/                        # Entorno virtual Python (contiene dependencias instaladas)

├── Proyecto_SMA/              # Configuración principal del proyecto Django
│   ├── __init__.py            # Marca esta carpeta como un paquete Python
│   ├── settings.py            # Configuración general del proyecto (DB, apps, seguridad, etc.)
│   ├── urls.py                # Rutas base del proyecto, incluye rutas de apps o Swagger
│   └── wsgi.py                # Punto de entrada WSGI para servidores de producción

├── reporte_ppda/              # App principal del sistema, gestiona medidas y avances PPDA
│   ├── __init__.py            # Marca esta carpeta como un paquete Python
│   ├── admin.py               # Configura cómo se muestran los modelos en el admin de Django
│   ├── apps.py                # Configuración de la app para Django
│   ├── models.py              # Modelos de base de datos: MedidaPPDA, AvanceMedida, Organismo
│   ├── serializers.py         # Serializadores DRF para convertir modelos a JSON
│   ├── views.py               # Lógica de la API (ViewSets para cada modelo)
│   ├── urls.py                # Endpoints API REST específicos de esta app
│   ├── permissions.py         # Reglas de acceso personalizadas (si aplica)
│   └── tests.py               # Pruebas automáticas del sistema

├── manage.py                  # Script principal para ejecutar comandos Django
├── requirements.txt           # Lista de paquetes necesarios para reproducir el entorno
├── .env                       # Variables secretas: usuario y clave de la base de datos, etc.
└── README.md                  # Documentación del proyecto y guía de instalación
```

---

## 🗄️ Estructura de Base de Datos (PostgreSQL - Supabase)

### 📌 Tabla: `reporte_ppda_organismo`

- Almacena las entidades públicas responsables de medidas PPDA.

### 📌 Tabla: `reporte_ppda_medidappda`

- Representa cada medida del PPDA, con tipo, indicador y organismo responsable.

### 📌 Tabla: `reporte_ppda_avancemedida`

- Registra reportes de avance por medida, con fecha, porcentaje y respaldo.

---

## 🧩 Estructura de modelos Django

```python
class Organismo(models.Model):
    nombre = models.CharField(max_length=200)         # Nombre del organismo
    comuna = models.CharField(max_length=100)         # Comuna asociada
    correo_contacto = models.EmailField()             # Correo oficial

class MedidaPPDA(models.Model):
    TIPO_CHOICES = [('regulatoria', 'Regulatoria'), ('no_regulatoria', 'No Regulatoria')]
    nombre = models.CharField(max_length=255)         # Nombre o título de la medida
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)  # Tipo de medida
    indicador = models.CharField(max_length=255)      # Indicador de seguimiento
    medio_verificacion = models.TextField()           # Evidencia del avance
    organismo_responsable = models.ForeignKey(Organismo, on_delete=models.CASCADE)  # FK

class AvanceMedida(models.Model):
    medida = models.ForeignKey(MedidaPPDA, on_delete=models.CASCADE)  # FK a Medida
    fecha_reporte = models.DateField()                                # Fecha de informe
    porcentaje_avance = models.PositiveIntegerField()                 # % acumulado
    observaciones = models.TextField(blank=True)                      # Comentarios
    archivo_respaldo = models.FileField(upload_to='reportes/', null=True, blank=True)  # Evidencia
```

---

---

## 🌐 Endpoints REST disponibles

| Método | URL                     | Descripción                  |
|--------|--------------------------|------------------------------|
| GET    | ``       | Listar organismos            |
| POST   | ``       | Crear un organismo           |
| GET    | ``          | Listar medidas               |
| POST   | ``          | Crear medida PPDA            |
| GET    | ``          | Listar avances               |
| POST   | ``          | Registrar avance             |

> Estos endpoints están protegidos con autenticación básica (pendiente de configuración) y permiten realizar operaciones CRUD sobre los modelos del sistema.
---

## 📄 Documentación de la API

La API cuenta con documentación interactiva generada automáticamente con Swagger y ReDoc:

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc UI: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

Para verla, asegúrate de ejecutar primero:

```bash
python manage.py runserver
```

Y de tener las siguientes librerías instaladas:

```bash
pip install drf-yasg
```
---

## 🔍 Funcionalidad de los endpoints

### `/api/organismos/`
- `GET` : Lista todos los organismos responsables registrados (ej: Seremi, CONAF).
- `POST` : Crea un nuevo organismo con nombre, comuna y correo de contacto.
- `PUT` : Reemplaza completamente un organismo existente.
- `PATCH` : Modifica parcialmente un organismo.
- `DELETE` : Elimina un organismo existente.

### `/api/medidas/`
- `GET` : Lista todas las medidas del PPDA, mostrando tipo, indicador y organismo responsable.
- `POST` : Crea una nueva medida PPDA asignada a un organismo.
- `PUT` : Reemplaza una medida existente.
- `PATCH` : Modifica parcialmente una medida.
- `DELETE` : Elimina una medida registrada.

### `/api/avances/`
- `GET` : Muestra los reportes de avance ingresados por cada organismo.
- `POST` : Registra un avance con porcentaje, observaciones y archivo respaldo.
- `PUT` : Reemplaza un avance completo.
- `PATCH` : Actualiza campos específicos de un avance.
- `DELETE` : Borra un avance registrado.

> Todos los endpoints permiten operaciones CRUD completas y están protegidos con autenticación básica.
### ``
- `GET`: Lista todos los organismos responsables registrados (ej: Seremi, CONAF).
- `POST`: Crea un nuevo organismo con nombre, comuna y correo de contacto.
- `PUT`: Reemplaza completamente un organismo existente.
- `PATCH`: Modifica parcialmente un organismo.
- `DELETE`: Elimina un organismo existente.

### ``
- `GET`: Lista todas las medidas del PPDA, mostrando tipo, indicador y organismo responsable.
- `POST`: Crea una nueva medida PPDA asignada a un organismo.
- `PUT`: Reemplaza una medida existente.
- `PATCH`: Modifica parcialmente una medida.
- `DELETE`: Elimina una medida registrada.

### ``
- `GET`: Muestra los reportes de avance ingresados por cada organismo.
- `POST`: Registra un avance con porcentaje, observaciones y archivo respaldo.
- `PUT`: Reemplaza un avance completo.
- `PATCH`: Actualiza campos específicos de un avance.
- `DELETE`: Borra un avance registrado.

> Todos los endpoints permiten operaciones CRUD completas y están protegidos con autenticación básica.

### ``
- `GET`: Lista todos los organismos responsables registrados (ej: Seremi, CONAF).
- `POST`: Crea un nuevo organismo con nombre, comuna y correo de contacto.

### ``
- `GET`: Lista todas las medidas del PPDA, mostrando tipo, indicador y organismo responsable.
- `POST`: Crea una nueva medida PPDA asignada a un organismo.

### ``
- `GET`: Muestra los reportes de avance ingresados por cada organismo.
- `POST`: Registra un avance con porcentaje, observaciones y archivo respaldo.

> Todos los endpoints están protegidos con autenticación básica.
---

## 🧠 Relaciones entre Tablas y Utilidad

A continuación se detalla la estructura de la base de datos según el diagrama generado en Supabase:

### 🏢 `reporte_ppda_organismo`
- Almacena los organismos responsables.
- Relacionada con `medidappda` a través de `organismo_responsable_id`.

### 📋 `reporte_ppda_medidappda`
- Representa medidas del PPDA.
- Relacionada con `organismo` y utilizada por `avance_medida`.

### 📈 `reporte_ppda_avancemedida`
- Registra el progreso de las medidas.
- Relacionada con `medidappda` a través de `medida_id`.

### 🔐 Tablas de usuarios (`auth_user`, `auth_group`, etc.)
- Gestionan usuarios, permisos y sesiones del sistema.
- Permiten aplicar autenticación básica en los endpoints.

> Estas relaciones permiten seguir el modelo lógico del PPDA definido en la Instrucción General de la SMA, permitiendo trazabilidad completa desde el organismo responsable hasta el avance reportado con evidencia.

---

## 📊 Estructura relacional de la base de datos

La base de datos está compuesta por tres tablas principales, reflejando los lineamientos de la Instrucción General de la SMA:

- **`reporte_ppda_organismo`**  
  Almacena la información de los organismos responsables de ejecutar medidas del PPDA. Contiene nombre, comuna y correo de contacto.

- **`reporte_ppda_medidappda`**  
  Registra cada medida definida en el PPDA. Incluye tipo, indicador, medio de verificación y una relación directa al organismo responsable.

- **`reporte_ppda_avancemedida`**  
  Permite registrar reportes de avance en fechas determinadas, asociados a una medida. Guarda fecha, porcentaje de avance, observaciones y respaldo.

Además, las tablas de Django como `auth_user`, `auth_group` y `django_session` gestionan la autenticación básica y sesiones activas en el sistema.

Esta estructura permite mantener trazabilidad completa entre organismos, medidas y avances, cumpliendo con los requisitos de reporte establecidos por la SMA.