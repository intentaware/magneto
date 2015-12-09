from django.conf.urls import patterns, include, url
from .routes import router

urlpatterns = patterns(
    'campaigns',
    url('', include(router.urls)),

)
