from rest_framework import routers
from django.urls import path
from .api import *

# Con router y la configuracion del UserViewSet y GroupViewSet permite crear automaticamente el CRUD
# para la clase User y Group
router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('groups', GroupViewSet, 'groups')

urlpatterns = router.urls

urlpatterns += [
    path("profile/", UserProfileViewSet.as_view(), name="profile"),
    path("permissions/", PermissionViewSet.as_view(), name="permissions"),
    path("update_groups/", UpdateUserGroupViewSet.as_view(), name="update groups"),
    path("update_permissions/", UpdateUserPermissionsViewSet.as_view(), name="update permissions"),
]