from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'adomatic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # adomattic urls
    url(r'^api/', include('apps.api.urls', namespace='api')),
    url(r'^users/', include('apps.users.urls')),
    url(r'^dashboard/', include('apps.dashboard.urls')),
)

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
