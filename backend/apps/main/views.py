from rest_framework import viewsets
from .models import *
from .serializers import *


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


class NationalsViewSet(viewsets.ModelViewSet):
    queryset = Nationals.objects.all()
    serializer_class = NationalsSerializer


class RegistrationstateViewSet(viewsets.ModelViewSet):
    queryset = Registrationstate.objects.all()
    serializer_class = RegistrationstateSerializer


class AsbViewSet(viewsets.ModelViewSet):
    queryset = Asb.objects.all()
    serializer_class = AsbSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

