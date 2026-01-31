from django.contrib import admin
from django.urls import path, include
from .views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('products/', ProductListView.as_view(), name='product-list'),
]