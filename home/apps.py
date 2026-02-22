from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        # This tells Django: "When the app starts, look at signals.py"
        import home.signals