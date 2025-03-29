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

- **Propósito**: Almacena las entidades públicas responsables de medidas PPDA.
- **Campos**:
  - `nombre`: Nombre del organismo (Ej: Seremi Salud, CONAF).
  - `comuna`: Comuna responsable.
  - `correo_contacto`: Email oficial de contacto.

---

### 📌 Tabla: `reporte_ppda_medidappda`

- **Propósito**: Representa cada medida del PPDA que debe ser implementada.
- **Campos**:
  - `nombre`: Descripción de la medida.
  - `tipo`: Regulatoria o No Regulatoria.
  - `indicador`: Cómo se mide el avance.
  - `medio_verificacion`: Documentos o acciones que respaldan el cumplimiento.
  - `organismo_responsable`: Relación con la tabla `organismo`.

---

### 📌 Tabla: `reporte_ppda_avancemedida`

- **Propósito**: Permite registrar los reportes de avance por cada medida en fechas determinadas.
- **Campos**:
  - `medida`: Relación con la medida del PPDA.
  - `fecha_reporte`: Fecha del avance informado.
  - `porcentaje_avance`: Avance numérico (%) acumulado.
  - `observaciones`: Detalles u observaciones del organismo.
  - `archivo_respaldo`: Documento adjunto como evidencia (opcional).

---

✅ Estas tablas ya se encuentran creadas y visibles en Supabase tras ejecutar las migraciones.

_Próximamente: endpoints REST, autenticación y documentación Swagger._