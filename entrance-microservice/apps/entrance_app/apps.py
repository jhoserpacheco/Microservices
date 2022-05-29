from django.apps import AppConfig


class EntranceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entrance_app'

class CoreConfig(AppConfig):
    name = 'entrance_app'
    label = 'entrance_app'