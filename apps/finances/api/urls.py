from django.conf.urls import patterns, include, url
from .routes import router

urlpatterns = patterns(
    '',
    url('', include(router.urls)),
)
