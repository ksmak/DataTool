from django.db import connection
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Database,
    Dictionary,
)
from .serializers import (
    DatabaseSerializer,
    DictionarySerializer
)


class DictionaryViewSet(viewsets.ReadOnlyModelViewSet):
    """Dictionary viewset"""

    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


class DatabaseViewSet(viewsets.ReadOnlyModelViewSet):
    """Database viewset"""

    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer


class GenerateView(APIView):
    """Generate db view"""

    def post(self, request):
        db_id = request.data.get('db_id')

        if not db_id:
            return Response({
                'status': 'failed',
                'error': '<db_id> parameter not found'
            })

        database = Database.objects.filter(id=db_id).first()

        if not database:
            return Response({
                'status': 'failed',
                'error': 'database not found'
            })

        serializer = DatabaseSerializer(database)

        if not serializer:
            return Response({
                'status': 'failed',
                'error': 'serialization error'
            })

        # with connection.cursor() as cursor:
        #     cursor.execute("CALL test_procedure('%s')", [1])
        #     cursor.execute('select * from abstracts_database')
        #     row = cursor.fetchone()

        return Response({
            'status': 'success',
            'data': serializer.data
        })
