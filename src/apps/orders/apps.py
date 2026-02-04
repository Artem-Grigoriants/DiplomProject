#Код `apps.py` определяет конфигурацию приложения `orders`.
#Он задаёт метаданные, такие как имя приложения и тип поля первичного ключа по умолчанию.
from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'