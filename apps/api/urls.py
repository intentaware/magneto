from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'api',
    url(r'^users/', include('apps.users.api.urls')),
    url(r'^campaigns/', include('apps.campaigns.api.urls')),
    url(r'^impressions/', include('apps.impressions.api.urls')),
)
