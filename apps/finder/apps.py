from django.apps import AppConfig


class FinderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.finder"

    def ready(self):
        import apps.finder.signals
