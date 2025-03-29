# 🛠️ Proyecto SMA - Registro y Reporte PPDA CQP

Este proyecto permite a organismos responsables registrar y reportar el estado de avance de las medidas del Plan de Prevención y Descontaminación Atmosférica (PPDA) para las comunas de Concón, Quintero y Puchuncaví, según lo instruido por la SMA en la Resolución Exenta N°1379.

---

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

## ✅ Configuración inicial del proyecto

### 1. Crear entorno virtual

```bash
python -m venv env
```

### 2. Activar entorno virtual

```bash
.\env\Scripts\Activate.ps1
```

---

### 3. Instalar dependencias

```bash
pip install django djangorestframework psycopg2-binary drf-yasg python-decouple
```

---

### 4. Crear proyecto Django

```bash
django-admin startproject Proyecto_SMA .
```

> ⚠️ El punto `.` al final evita duplicar el nombre de carpeta del proyecto.

---

### 5. Crear la aplicación principal

```bash
python manage.py startapp reporte_ppda
```

---

### 6. Registrar apps en `Proyecto_SMA/settings.py`

```python
INSTALLED_APPS = [
    'rest_framework',
    'drf_yasg',
    'reporte_ppda',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

### 7. Crear archivo `.env` en la raíz

```env
DB_NAME=nombre_basedatos
DB_USER=usuario
DB_PASSWORD=clave
DB_HOST=localhost
DB_PORT=5432
```

---

_Próximamente: configuración de base de datos PostgreSQL y creación de modelos._