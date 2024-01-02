from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from .models import (
    Department,
    Database,
    Dictionary,
)
from .serializers import (
    DepartmentSerializer,
    DictionarySerializer,
)
from auths.models import DatabaseAccess, FormAccess, UserRole


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """Department viewset"""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DictionaryViewSet(viewsets.ReadOnlyModelViewSet):
    """Dictionary viewset"""

    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


class DbListView(APIView):
    """Database list view"""

    permission_classes = [AllowAny]

    def get(self, request):
        result = []
        databases = Database.objects.all()
        for db in databases:
            result.append({
                "id": db.id,
                "title": db.title,
            })

        return Response(result)


class DbStructView(APIView):
    """Database structure view"""

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user_roles = UserRole.objects.filter(user=request.user)
        role_ids = [user_role.role.id for user_role in user_roles]
        dba = DatabaseAccess.objects.filter(
            role__in=role_ids, database=pk).first()

        if not dba:
            return Response(
                {'error': 'Database not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        db_struct = dba.database.struct
        for form in db_struct['forms']:
            frma = FormAccess.objects.filter(
                role__in=role_ids, form=form['id']).first()
            form['access_type'] = frma.access_type if frma else None

        return Response(db_struct)
