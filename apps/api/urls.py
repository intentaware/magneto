from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'api',
    url(r'^users/', include('apps.users.api.urls')),
    url(r'^ads/', include('apps.ads.api.urls')),
)
