from rest_framework import viewsets
from .models import Organismo, MedidaPPDA, AvanceMedida
from .serializers import OrganismoSerializer, MedidaPPDASerializer, AvanceMedidaSerializer

class OrganismoViewSet(viewsets.ModelViewSet):
    queryset = Organismo.objects.all()
    serializer_class = OrganismoSerializer

class MedidaPPDAViewSet(viewsets.ModelViewSet):
    queryset = MedidaPPDA.objects.all()
    serializer_class = MedidaPPDASerializer

class AvanceMedidaViewSet(viewsets.ModelViewSet):
    queryset = AvanceMedida.objects.all()
    serializer_class = AvanceMedidaSerializer
