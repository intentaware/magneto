from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'api',
    url(r'^users/', include('apps.users.api.urls')),
)
