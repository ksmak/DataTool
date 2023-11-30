from rest_framework import viewsets
from .models import *
from .serializers import *


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class AsbViewSet(viewsets.ModelViewSet):
    queryset = Asb.objects.all()
    serializer_class = AsbSerializer

