from django.apps import AppConfig

class MainConfig(AppConfig):
    name='jobs.apps'

    def ready(self):
        from jobs import updater
        updater.start()