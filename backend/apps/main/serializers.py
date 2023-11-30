from rest_framework import serializers
from .models import *


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class AsbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asb
        fields = "__all__"

