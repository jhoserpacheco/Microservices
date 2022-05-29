from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from apps.user_app.models import User
from django.contrib.auth.models import Permission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated] #, permissions.IsAdminUser]
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated] #, permissions.IsAdminUser]
    serializer_class = GroupSerializer

class PermissionViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated] #, permissions.IsAdminUser]

    def get(self, request):
        permissions = Permission.objects.filter(
            content_type__app_label='user_app', 
            content_type__model='user', 
            codename__startswith='app_'
        )
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

class UpdateUserGroupViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated] #, permissions.IsAdminUser]

    def put(self, request):
        user_group_serializer = UpdateUserGroupSerializer(data=request.data)
        if user_group_serializer.is_valid():
            user_id = user_group_serializer.validated_data['user_id']
            groups = user_group_serializer.validated_data['groups']
            user = User.objects.get(id=user_id)
            user.groups.set(groups)
            return Response(status=200)
        else:
            return Response(user_group_serializer.errors, status=400)

class UpdateUserPermissionsViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated] #, permissions.IsAdminUser]

    def put(self, request):
        user_permissions_serializer = UpdateUserPermissionsSerializer(data=request.data)
        if user_permissions_serializer.is_valid():
            user_id = user_permissions_serializer.validated_data['user_id']
            user_permissions = user_permissions_serializer.validated_data['user_permissions']
            user = User.objects.get(id=user_id)
            user.user_permissions.set(user_permissions)
            return Response(status=200)
        else:
            return Response(user_permissions_serializer.errors, status=400)

class UserProfileViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user = User.objects.get(id=user.id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    
    #Not implemented yet
    def put(self, request):
        user = request.user
        user = User.objects.get(id=user.id)
        serializer = UpdateUserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)