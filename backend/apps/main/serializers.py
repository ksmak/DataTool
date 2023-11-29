from rest_framework import serializers
from .models import (
    Department,
    Dictionary,
    Database,
    Form,
    Group,
    Field,
    Report,
    Converter
)


class ReportSerializer(serializers.ModelSerializer):
    """Report serializer"""

    class Meta:
        model = Report
        fields = '__all__'


class ConverterSerializer(serializers.ModelSerializer):
    """Converter serializer"""

    class Meta:
        model = Converter
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    """Field serializer"""

    class Meta:
        model = Field
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Group serializer"""

    fields = FieldSerializer(many=True)

    class Meta:
        model = Group
        fields = (
            'id',
            'order',
            'title',
            'is_multy',
            'table_name',
            'fields'
        )


class FormSerializer(serializers.ModelSerializer):
    """Form serializer"""

    groups = GroupSerializer(many=True)

    class Meta:
        model = Form
        fields = (
            'id',
            'order',
            'title',
            'form_type',
            'groups',
        )


class DatabaseSerializer(serializers.ModelSerializer):
    """Database serializer"""

    forms = FormSerializer(many=True)
    reports = ReportSerializer(many=True)
    converters = ConverterSerializer(many=True)

    class Meta:
        model = Database
        fields = (
            'id',
            'order',
            'title',
            'forms',
            'reports',
            'converters'
        )


class DictionarySerializer(serializers.ModelSerializer):
    """Dictionary serializer"""

    class Meta:
        model = Dictionary
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    """Department serializer"""

    class Meta:
        model = Department
        fields = '__all__'
