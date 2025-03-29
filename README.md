# 🛠️ Proyecto SMA - Registro y Reporte PPDA CQP

Este proyecto permite a organismos responsables registrar y reportar el estado de avance de las medidas del Plan de Prevención y Descontaminación Atmosférica (PPDA) para las comunas de Concón, Quintero y Puchuncaví, según lo instruido por la SMA en la Resolución Exenta N°1379.

---

## 🗂️ Estructura de archivos del proyecto

```
M5 - 3 - APP SMA/
├── env/                        # Entorno virtual
├── Proyecto_SMA/              # Configuración principal de Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── reporte_ppda/              # Aplicación del proyecto
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   └── tests.py
├── manage.py
├── requirements.txt
├── .env
└── README.md
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