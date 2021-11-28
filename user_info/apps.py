from django.apps import AppConfig


class UserInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_info'

    def ready(self):
        from . import signals  # NOQA
