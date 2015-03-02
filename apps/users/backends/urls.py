from django.conf.urls import patterns, include, url
#from django.views.generic.base import TemplateView
from .views import UserRegistrationView, CompanyRegistrationView


urlpatterns = patterns('', 
    url(r'^register/$', 
        UserRegistrationView.as_view(), name='registration_register',),
    url(r'^company/$', 
        CompanyRegistrationView.as_view(), name='registration_company'),    
    (r'', include('registration.auth_urls')),
    )