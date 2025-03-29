from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganismoViewSet, MedidaPPDAViewSet, AvanceMedidaViewSet

# Crear router para los endpoints REST
router = DefaultRouter()
router.register(r'organismos', OrganismoViewSet)
router.register(r'medidas', MedidaPPDAViewSet)
router.register(r'avances', AvanceMedidaViewSet)

# Incluir las rutas del router
urlpatterns = [
    path('', include(router.urls)),
]
