from rest_framework import viewsets

from .models import (
    Department,
    Database,
    Dictionary,
)
from .serializers import (
    DepartmentSerializer,
    DatabaseSerializer,
    DictionarySerializer
)


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """Department viewset"""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DictionaryViewSet(viewsets.ReadOnlyModelViewSet):
    """Dictionary viewset"""

    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


class DatabaseViewSet(viewsets.ReadOnlyModelViewSet):
    """Database viewset"""

    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer
