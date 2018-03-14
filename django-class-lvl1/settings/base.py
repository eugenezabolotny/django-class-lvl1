import sys
import os
from os.path import join, abspath, dirname

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# PATH vars

# here = lambda *x: join(abspath(dirname(__file__)), *x)
def here(*x): return join(abspath(dirname(__file__)), *x)


PROJECT_ROOT = here("..")


# root = lambda *x: join(abspath(PROJECT_ROOT), *x)
def root(*x): return join(abspath(PROJECT_ROOT), *x)


sys.path.insert(0, root('apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE THIS!!!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'todo',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

PROJECT_APPS = []

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django-class-lvl1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
            # 'DEBUG': DEBUG,
            # 'TEMPLATE_DEBUG': DEBUG
        },
    },
]

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django-class-lvl1.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-class-lvl1',
        'USER': 'postgres',
        'PASSWORD': '098-098',
        'HOST': 'localhost',  # '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s; %(filename)s:%(lineno)d] '
                      '%(levelname)s:%(name)s: \n\t%(message)s ',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'  # 'Europe/London'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = root('assets', 'uploads')
MEDIA_URL = '/media/'

# Additional locations of static files

STATICFILES_DIRS = (
    root('assets'),
)

# TEMPLATE_DIRS = (
#     root('templates'),
# )


# .local.py overrides all the common settings.
try:
    from .local import *  # NOQA
except ImportError:
    pass

# importing test settings file if necessary
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    from .testing import *  # NOQA

# Debug toolbar
if DEBUG:
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INSTALLED_APPS += ["debug_toolbar",
                       "django_coverage"]
