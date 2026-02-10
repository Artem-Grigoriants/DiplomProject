from django.urls import path
from .views import RollbarTestView

urlpatterns = [
    path('rollbar-test/', RollbarTestView.as_view(), name='rollbar-test'),
]

