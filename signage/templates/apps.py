from django.apps import AppConfig


class TemplatesAppConfig(AppConfig):

    name = "signage.templates"
    verbose_name = "Templates"

    def ready(self):
        try:
            import menus.signals  # noqa F401
        except ImportError:
            pass
