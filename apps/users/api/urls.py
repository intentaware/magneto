from django.conf.urls import patterns, include, url

from .views import UserRegistrationView, CompanyRegistrationView

urlpatterns = patterns(
    'users',
    #url(r'^register/user/$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^register/company/$', CompanyRegistrationView.as_view(), name='register_company')
)


