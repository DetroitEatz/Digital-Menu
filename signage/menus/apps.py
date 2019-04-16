from django.apps import AppConfig


class MenusAppConfig(AppConfig):

    name = "signage.menus"
    verbose_name = "Menus"

    def ready(self):
        try:
            import menus.signals  # noqa F401
        except ImportError:
            pass
