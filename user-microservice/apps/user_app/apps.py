from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_app'

class CoreConfig(AppConfig):
    name = 'user_app'
    label = 'user_app'