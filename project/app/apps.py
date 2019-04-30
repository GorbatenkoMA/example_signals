from django.apps import AppConfig
# from django.db.models.signals import post_save


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        # import app.signals
        from . import signals
