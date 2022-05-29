from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_app'

class CoreConfig(AppConfig):
    name = 'auth_app'
    label = 'auth_app'