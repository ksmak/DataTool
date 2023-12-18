from rest_framework import serializers
from .models import *


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AsbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asb
        fields = "__all__"

