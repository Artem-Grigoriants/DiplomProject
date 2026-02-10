#Код определяет конфигурацию приложения `users` в вашем проекте Django.
#Он задаёт метаданные и настройки для приложения.

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        import apps.users.signals
