from django.conf.urls import patterns, include, url

from .views import GetImpression

urlpatterns = patterns(
    'impressions',
    #url(r'^register/user/$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^i/$', GetImpression.as_view(), name='get_new_impression'),
    url(r'^i/(?P<pk>\d+)/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', GetImpression.as_view(), name='claim_coupon')
)
