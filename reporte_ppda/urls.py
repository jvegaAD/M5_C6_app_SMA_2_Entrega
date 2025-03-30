from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, OrganismoViewSet, MedidaPPDAViewSet, AvanceMedidaViewSet

router = DefaultRouter()
router.register(r'organismos', OrganismoViewSet)
router.register(r'medidas', MedidaPPDAViewSet)
router.register(r'avances', AvanceMedidaViewSet)

urlpatterns = [
    path('', home),               # Vista principal (landing page)
    path('api/', include(router.urls)),  # Endpoints REST
]
