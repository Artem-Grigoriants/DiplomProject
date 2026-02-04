#Код определяет конфигурацию приложения `products`
#Он задаёт метаданные и настройки для приложения.

from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'