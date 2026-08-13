from rest_framework import serializers

from user.models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "password",
            "created_at",
            "updated_at",
            "address",
            "role",
        ]
        read_only_fields = ["created_at"]
        extra_kwargs = {"password": {"write_only": True}}
