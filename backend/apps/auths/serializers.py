from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        return {
            "access": data["access"],
            "refresh": data["refresh"],
            "user": {
                "id": self.user.id,
                "username": self.user.get_username(),
                "fullName": self.user.full_name,
            }
        }
