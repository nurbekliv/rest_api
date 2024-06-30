from django.apps import AppConfig


class MygovConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mygov'


class MygovConfig2(AppConfig):
    name = 'mygov'

    def ready(self):
        import mygov.signals
