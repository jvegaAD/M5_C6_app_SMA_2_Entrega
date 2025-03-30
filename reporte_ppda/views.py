from django.http import HttpResponse
from rest_framework import viewsets
from .models import Organismo, MedidaPPDA, AvanceMedida
from .serializers import OrganismoSerializer, MedidaPPDASerializer, AvanceMedidaSerializer

def home(request):
    contenido_html = """
    <html>
        <head><meta charset="utf-8"><title>PPDA SMA</title></head>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h1>🐍 Curso Backend Python</h1>
            <h2>👥 Grupo 8</h2>
            <h3>📌 Detalle de la tarea</h3>
            <h4>🧱 Levantamiento / Diseño / Implementación de la Base de Datos</h4>
            <ul>
                <li>Cada grupo deberá elegir o crear una <strong>historia de usuario</strong> generada para el proyecto.</li>
                <li>Crear <strong>modelos en Django</strong> para representar las entidades (o usar FastAPI si se prefiere).</li>
                <li>Aplicar <strong>migraciones</strong> para crear las tablas en la base de datos.</li>
            </ul>
            <h4>📦 Productos esperados</h4>
            <ul>
                <li>📝 Historia de usuario a desarrollar.</li>
                <li>⚙️ Proyecto Django (o FastAPI) creado.</li>
                <li>🧩 Modelos definidos con sus relaciones clave.</li>
                <li>🗃️ Base de datos con tablas creadas.</li>
            </ul>
            <h3>🚀 Desarrollo de Endpoints</h3>
            <ul>
                <li>Crear al menos <strong>dos endpoints</strong> usando <strong>DRF</strong> o <strong>FastAPI</strong>.</li>
                <li>Deben incluir <strong>un método POST y otro GET</strong>.</li>
                <li>Agregar <strong>autenticación básica</strong> a los endpoints.</li>
                <li>Probar los endpoints con <strong>Postman</strong>.</li>
                <li>Documentar los endpoints usando <strong>Swagger</strong>.</li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(contenido_html)

class OrganismoViewSet(viewsets.ModelViewSet):
    queryset = Organismo.objects.all()
    serializer_class = OrganismoSerializer

class MedidaPPDAViewSet(viewsets.ModelViewSet):
    queryset = MedidaPPDA.objects.all()
    serializer_class = MedidaPPDASerializer

class AvanceMedidaViewSet(viewsets.ModelViewSet):
    queryset = AvanceMedida.objects.all()
    serializer_class = AvanceMedidaSerializer
