from django.apps import AppConfig


# class StudentgConfig(AppConfig):
#     name = 'studentg'

class StudentgConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studentg'


    def ready(self):
        import studentg.signals


