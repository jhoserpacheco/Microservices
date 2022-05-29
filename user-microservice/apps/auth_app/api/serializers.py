from tokenize import group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer, ValidationError
from rest_framework_simplejwt.state import token_backend
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from apps.user_app.models import User

#Serializing all models to sharing the data in REST format

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'codename',)

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions',)

class TokenUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    user_permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'is_active', 'groups','user_permissions',)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Si se quiere agregar algo al token
        # ...
        token['user'] = TokenUserSerializer(user).data

        return token

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(MyTokenRefreshSerializer, self).validate(attrs)
        
        # En caso de que se requiera personalizar el token de refresh
        #decoded_payload = token_backend.decode(data['access'], verify=True)
        #user_uid=decoded_payload['user_id']

        return data