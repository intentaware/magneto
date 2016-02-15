from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^auth/', include('apps.users.backends.urls')),
    # TODO, replace with custom backend
)
