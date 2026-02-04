#Код определяет шаблоны URL-адресов для приложения `products`.
#Он сопоставляет конкретные пути URL-адресов с соответствующими представлениями,
#позволяя приложению обрабатывать HTTP-запросы к конечным точкам
from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
]