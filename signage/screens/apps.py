from django.apps import AppConfig


class ScreenAppConfig(AppConfig):

    name = "signage.screens"
    verbose_name = "Screens"

    def ready(self):
        try:
            import screens.signals  # noqa F401
        except ImportError:
            pass
