from django.conf.urls import patterns, include, url
#from django.views.generic.base import TemplateView
from .views import UserRegistrationView


urlpatterns = patterns('', 
    url(r'^register/$', 
        UserRegistrationView.as_view(), name='registration_user'),
    #url(r'^register/closed/$',  TemplateView.as_view(template_name='registration/registration_closed.html'),name='registration_disallowed'),
    (r'', include('registration.auth_urls')),
)