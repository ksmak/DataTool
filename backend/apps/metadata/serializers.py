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

    fields = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = (
            'id',
            'pos',
            'title',
            'is_multy',
            'table_name',
            'fields2'
        )

    def get_fields(self, instance):
        fields = instance.fields.all().order_by("-pos")
        return FieldSerializer(fields, many=True).data


class FormSerializer(serializers.ModelSerializer):
    """Form serializer"""

    groups = serializers.SerializerMethodField()

    class Meta:
        model = Form
        fields = (
            'id',
            'pos',
            'title',
            'form_type',
            'groups',
        )

    def get_groups(self, instance):
        groups = instance.groups.all().order_by("-pos")
        return GroupSerializer(groups, many=True).data


class DatabaseSerializer(serializers.ModelSerializer):
    """Database serializer"""

    forms = FormSerializer(many=True)
    reports = ReportSerializer(many=True)
    converters = ConverterSerializer(many=True)

    class Meta:
        model = Database
        fields = (
            'id',
            'pos',
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
