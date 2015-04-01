from base import *

SITE_ID = 1

INSTALLED_APPS += (
    'rest_framework',
)

INTERNAL_IPS = (
    '0.0.0.0', '127.0.0.1'
)

STATIC_URL = '/static/'
MEDIA_URL = 'http://localhost:9050/media/'
