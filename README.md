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

_Próximamente: implementación de endpoints, autenticación y Swagger._
---

## 🌐 Endpoints REST disponibles

| Método | URL                     | Descripción                  |
|--------|--------------------------|------------------------------|
| GET    | `/api/organismos/`       | Listar organismos            |
| POST   | `/api/organismos/`       | Crear un organismo           |
| GET    | `/api/medidas/`          | Listar medidas               |
| POST   | `/api/medidas/`          | Crear medida PPDA            |
| GET    | `/api/avances/`          | Listar avances               |
| POST   | `/api/avances/`          | Registrar avance             |

> Estos endpoints están protegidos con autenticación básica (pendiente de configuración) y permiten realizar operaciones CRUD sobre los modelos del sistema.