from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from reporte_ppda.views import home  # 👈 Importar la vista

schema_view = get_schema_view(
    openapi.Info(
        title="API PPDA SMA",
        default_version='v1',
        description="Documentación del sistema de avance del PPDA (Concón, Quintero y Puchuncaví)",
        contact=openapi.Contact(email="contacto@sma.cl"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home, name='home'),  # 👈 Ruta de inicio configurada
    path('admin/', admin.site.urls),
    path('api/', include('reporte_ppda.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
