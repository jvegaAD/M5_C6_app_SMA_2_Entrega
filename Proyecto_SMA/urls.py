# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('reporte_ppda.urls')),
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# IMPORTAR PARA DOCUMENTACIÓN
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# CONFIGURACIÓN DE LA DOCUMENTACIÓN
schema_view = get_schema_view(
    openapi.Info(
        title="PPDA SMA API",
        default_version='v1',
        description="Documentación de la API del proyecto PPDA",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('reporte_ppda.urls')),  # home y router API
    path('admin/', admin.site.urls),
    path('api/', include('reporte_ppda.urls')),

    # DOCUMENTACIÓN
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
