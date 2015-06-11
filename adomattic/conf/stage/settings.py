from base import *

SITE_ID = 1

DEBUG = False

INSTALLED_APPS += (
    'rest_framework',
    'django.contrib.staticfiles',
)

STATIC_URL = 'http://app.adomattic.com/static/'
MEDIA_URL = 'http://app.adomattic.com/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vader',
        'USER': 'django',
        'PASSWORD': 'DZn#kF^zdMcAsmytQEVKe7!w',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STRIPE_KEY = 'sk_test_s0cxlb2a5kArqUwfSGeig5CI'
