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

AWS_STORAGE_BUCKET_NAME = 'vader-faith'
AWS_ACCESS_KEY_ID = 'AKIAI23OY6DM5YW6IWIA'
AWS_SECRET_ACCESS_KEY = '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'

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

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
