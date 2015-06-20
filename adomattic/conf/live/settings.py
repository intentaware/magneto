from base import *

SITE_ID = 1

DEBUG = False

ALLOWED_HOSTS = [
    '.adomattic.com',  # Allow domain and subdomains
    '.adomattic.com.',  # Also allow FQDN and subdomains
]

INSTALLED_APPS += (
    'rest_framework',
    'django.contrib.staticfiles',
    'storages'
)

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://b1b9cb8df048483295724db97fadd76c:7f95b0b35c154327a0cd24d6638eb1d8@app.getsentry.com/45852',
}

STATIC_URL = 'http://app.adomattic.com/static/'
MEDIA_URL = 'http://app.adomattic.com/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vader',
        'USER': 'vader',
        'PASSWORD': 'axBPx97Xx2pNDnphPvf6kWwXmqNbP3SNjSKVs32D',
        'HOST': 'vader.c3udwfzrnadp.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

STRIPE_KEY = 'sk_test_s0cxlb2a5kArqUwfSGeig5CI'
