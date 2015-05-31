from base import *

SITE_ID = 1

INSTALLED_APPS += (
    'rest_framework',
    'devserver',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES += (
    'devserver.middleware.DevServerMiddleware',
)

INTERNAL_IPS = (
    '0.0.0.0', '127.0.0.1'
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vader',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
)

DEVSERVER_TRUNCATE_SQL = False

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

STRIPE_KEY = 'sk_test_s0cxlb2a5kArqUwfSGeig5CI'
