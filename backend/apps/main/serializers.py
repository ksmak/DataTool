from rest_framework import serializers
from .models import *


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"


class NationalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationals
        fields = "__all__"


class RegistrationstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrationstate
        fields = "__all__"


class AsbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asb
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

