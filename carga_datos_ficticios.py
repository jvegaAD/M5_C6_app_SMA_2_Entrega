from reporte_ppda.models import Organismo, MedidaPPDA, AvanceMedida
from django.utils import timezone
import random
from datetime import timedelta

# Limpiar datos previos (opcional)
Organismo.objects.all().delete()
MedidaPPDA.objects.all().delete()
AvanceMedida.objects.all().delete()

# Crear organismos
organismos = []
for i in range(1, 11):
    org = Organismo.objects.create(
        nombre=f"Organismo {i}",
        comuna=random.choice(["Concón", "Quintero", "Puchuncaví"]),
        correo_contacto=f"organismo{i}@sma.cl"
    )
    organismos.append(org)

# Tipos de medida y medios de verificación simulados
tipos = ["Regulación", "Fomento", "Estudios", "Educación", "Política Pública"]
medios_verificacion = [
    "Registro interno",
    "Informe técnico",
    "Base de datos de emisiones",
    "Formulario de actividades",
    "Reporte consolidado anual"
]

# Crear medidas (30 medidas)
medidas = []
for i in range(1, 31):
    medida = MedidaPPDA.objects.create(
        nombre=f"Medida {i} - Mejora ambiental sectorial",
        tipo=random.choice(["regulatoria", "no_regulatoria"]),
        indicador=f"Indicador específico {i}",
        medio_verificacion=random.choice(medios_verificacion),
        organismo_responsable=random.choice(organismos)
    )
    medidas.append(medida)

# Crear avances (90 reportes, 3 por medida)
for medida in medidas:
    for j in range(3):
        fecha = timezone.now().date() - timedelta(days=random.randint(10, 365))
        porcentaje = random.randint(10, 100)
        observaciones = f"Avance parcial ({porcentaje}%) registrado el {fecha}"
        AvanceMedida.objects.create(
            medida=medida,
            fecha_reporte=fecha,
            porcentaje_avance=porcentaje,
            observaciones=observaciones,
            archivo_respaldo=None
        )

print("Datos ficticios cargados correctamente.")