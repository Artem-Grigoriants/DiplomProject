#Код файла `urls.py` определяет шаблоны URL-адресов для приложения `orders`.
#Он сопоставляет определенные пути URL-адресов с соответствующими представлениями.

from django.urls import path
from .views import (
    CartView,
    LoginView,
    RegistrationView,
    ProductListView,
    ContactView,
    OrderConfirmationView,
    OrderListView,
)

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>/', CartView.as_view(), name='cart-item'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('order/confirm/', OrderConfirmationView.as_view(), name='order-confirmation'),
    path('', OrderListView.as_view(), name='order-list'),
]