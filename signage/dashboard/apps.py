from django.apps import AppConfig


class DashboardAppConfig(AppConfig):

    name = "signage.dashboard"
    verbose_name = "Dashboard"

    def ready(self):
        try:
            import dashboard.signals  # noqa F401
        except ImportError:
            pass
