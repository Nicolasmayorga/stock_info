import uuid
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    api_key = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'api_key']

    def create(self, validated_data):
        validated_data['api_key'] = uuid.uuid4().hex
        return super().create(validated_data)