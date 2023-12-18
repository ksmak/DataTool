from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (
    Department,
    Database,
    Dictionary,
)
from .serializers import (
    DepartmentSerializer,
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


class DatabaseViewSet(viewsets.ViewSet):
    """Database viewset"""

    permission_classes = [IsAuthenticated]
    queryset = Database.objects.all()

    def retrieve(self, request, pk=None):
        db = get_object_or_404(self.queryset, pk=pk)
        return Response(db.struct)
