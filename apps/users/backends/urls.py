from django.conf.urls import patterns, include, url
#from django.views.generic.base import TemplateView
from .views import UserRegistrationView, CompanyRegistrationView, PasswordResetView


urlpatterns = patterns(
    'registration',
    #url(r'^register/$',
    #    UserRegistrationView.as_view(), name='registration_register',),
    url(
        r'^register/$',
        CompanyRegistrationView.as_view(),
        name='registration_register',
    ),
    url(
        r'^password/reset/$',
        PasswordResetView.as_view(),
        name='registration_password_reset',
    ),
    url(r'', include('registration.auth_urls')),
    )
