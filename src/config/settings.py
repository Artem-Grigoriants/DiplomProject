#Основной конфигурационный файл приложения Django.
#Он содержит все настройки и конфигурации,
#необходимые для работы проекта.
import os
from pathlib import Path

# Базовый каталог
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройки безопасности
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

#Настройка кастомной модель пользователя
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.yandex.YandexOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# Установленные приложения
INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.orders',
    'apps.products',
    'apps.users',
    'apps.core',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_spectacular',
    'easy_thumbnails',
]

#Конфигурация REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',  # 100 запросов в день для анонимных пользователей
        'user': '1000/day', # 1000 запросов в день для авторизованных пользователей
    },
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Diploma Project API',
    'DESCRIPTION': 'API for the diploma project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
}

#Конфигурация Djoser**:
#Настраивает поведение библиотеки Djoser для аутентификации и управления пользователями.
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': False,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        'user_create': 'apps.users.serializers.CustomUserCreateSerializer',
        'user': 'apps.users.serializers.CustomUserSerializer',
    },
}

# Промежуточное ПО**:
# Отображает список промежуточного ПО,
# используемого в проекте для обработки запросов и ответов.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

# URL configuration
ROOT_URLCONF = 'config.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),  # Use env var when available
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'aeg19802402'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),  # will be 'db' inside Docker
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    },
    'test_postgres': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TEST_POSTGRES_DB', 'test_postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'aeg19802402'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    },
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# JET settings
JET_THEME = 'default'
JET_SIDE_MENU_COMPACT = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery configuration
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/1')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# When running tests, execute tasks locally (synchronously)
CELERY_TASK_ALWAYS_EAGER = os.environ.get('CELERY_TASK_ALWAYS_EAGER', 'False') == 'True'
CELERY_TASK_EAGER_PROPAGATES = True

# Thumbnail settings
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
        'product_small': {'size': (100, 100), 'crop': True},
        'product_medium': {'size': (300, 300), 'crop': True},
    },
}
THUMBNAIL_DEFAULT_STORAGE = 'easy_thumbnails.storage.ThumbnailFileSystemStorage'
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)

# Social Auth configuration
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', 'your-google-oauth2-key')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', 'your-google-oauth2-secret')

SOCIAL_AUTH_YANDEX_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_YANDEX_OAUTH2_KEY', 'your-yandex-oauth2-key')
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_YANDEX_OAUTH2_SECRET', 'your-yandex-oauth2-secret')

# Rollbar configuration
ROLLBAR = {
    'access_token': os.environ.get('ROLLBAR_ACCESS_TOKEN', 'b692e1ddf31040b8bbe03816147b3ecb'),
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}
