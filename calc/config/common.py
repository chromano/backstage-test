import os
from os.path import join
from distutils.util import strtobool
import dj_database_url
from configurations import Configuration


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    CALC_NATURAL_SUM_DIFFERENCE_LIMIT = 10

    INSTALLED_APPS = (
        'django.contrib.contenttypes',

        # Third party apps
        'rest_framework',

        # Local apps
        'calc.natural.apps.NaturalAppConfig',
    )

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ALLOWED_HOSTS = ["*"]
    ROOT_URLCONF = 'calc.urls'
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    WSGI_APPLICATION = 'calc.wsgi.application'

    ADMINS = (
        ('Author', 'carlos.romano@toptal.com'),
    )

    DATABASES = {
        'default': dj_database_url.config(default='sqlite://data.sqlite3')
    }

    # General
    APPEND_SLASH = False
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True

    TEMPLATES = [
    ]

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'no'))

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
    AUTH_PASSWORD_VALIDATORS = [
    ]

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }
    }

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
        'DATETIME_FORMAT': 'iso-8601',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'UNAUTHENTICATED_USER': None,
    }
