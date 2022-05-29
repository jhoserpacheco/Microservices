from apps.user_app.models import User, Program
from apps.auth_app.api.serializers import GroupSerializer, PermissionSerializer
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {'permissions': {'required': True}}

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)
    program = ProgramSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

class UpdateUserGroupSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('user_id', 'groups',)
        extra_kwargs = {'groups': {'required': True}}

class UpdateUserPermissionsSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('user_id', 'user_permissions',)
        extra_kwargs = {'user_permissions': {'required': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(read_only=True)
    groups = GroupSerializer(many=True, read_only=True)
    user_permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'picture', 'program', 'groups', 'user_permissions',)
        extra_kwargs = {'id': {'read_only': True, 'required': False}}

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)
        extra_kwargs = {"username": {"required": False}, "first_name": {"required": True}, "last_name": {"required": True}}