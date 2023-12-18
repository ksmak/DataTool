from rest_framework import viewsets
from .models import *
from .serializers import *


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AsbViewSet(viewsets.ModelViewSet):
    queryset = Asb.objects.all()
    serializer_class = AsbSerializer

