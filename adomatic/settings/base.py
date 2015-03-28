"""
Django settings for adomattic project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
CONF_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(CONF_DIR, os.pardir)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$r^ufp^!he)i22(@yw#+%y&%-)t3cdvipxbz4#s)g^5gifitt-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'registration',
    'taggit',
    'widget_tweaks',
    'corsheaders',

    # django photologue
    'photologue',
    'sortedm2m',
)

ADOMATIC_APPS = (
    'apps.common',
    'apps.users',
    'apps.companies',

    'apps.campaigns',
    'apps.impressions',
    'apps.brands',

    # for front end
    'apps.dashboard',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + ADOMATIC_APPS

MIDDLEWARE_CLASSES = (
    'apps.impressions.middleware.ImpressionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'adomatic.urls'

WSGI_APPLICATION = 'adomatic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Media files (All the uploads)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Authentication (and Registration-Redux)
AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/users/auth/login/'
LOGOUT_URL = ''
LOGIN_REDIRECT_URL = '/dashboard/'

ACCOUNT_ACTIVATION_DAYS = 30


# For Registration process to be called from WordPress
REGISTRATION_API_KEY = 'WP_nEhj6FkTJNiFfiS5moVeUE'

# CORS Headers https://github.com/ottoyiu/django-cors-headers

CORS_ORIGIN_REGEX_WHITELIST = ('^(http?://)?(\w+\.)?adomattic\.com$', )

CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken',
        'wp-api-key',
        'publisher-key',
    )

# Impression Engine

IMPRESSION_COOKIE_NAME = 'magneto'

try:
    from local import *
except ImportError:
    sys.exit('Unable to import environment specific settings, check if file local.py is properly placed')
