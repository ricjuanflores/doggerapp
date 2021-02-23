from rest_framework import serializers
from .models import User, Dog, Service, Schedule
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_walker', 'is_owner', 'is_admin']

    def get_is_admin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_walker', 'is_owner', 'is_admin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ['id', 'name', 'size', 'owner']


class ServiceSerializer(serializers.ModelSerializer):
    dogs = DogSerializer(many=True)
    type = serializers.SerializerMethodField()
    class Meta:
        model = Service
        fields = '__all__'

    def get_type(self, obj):
        return obj.get_type_display()

    
