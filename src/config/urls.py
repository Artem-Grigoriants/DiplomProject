#Файл `urls.py` отвечает за определение шаблонов URL-адресов,
# которые направляют входящие HTTP-запросы к соответствующим представлениям.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders/', include('apps.orders.urls')),
    path('api/products/', include('apps.products.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]