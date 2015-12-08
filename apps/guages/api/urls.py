from django.conf.urls import patterns, include, url
from .routes import router
from .views import PostMatric

urlpatterns = patterns(
    'guages',
    url(r'^g/(?P<asset_id>.+)/$', PostMatric.as_view(), name='post_matric'),
    url('', include(router.urls)),
)
