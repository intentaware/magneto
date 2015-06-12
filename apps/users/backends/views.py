from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView

from registration.backends.simple.views import \
    RegistrationView as BaseRegistrationView
from registration import signals

from .forms import UserCreationForm, CompanyCreationForm

from apps.users.models import User
from apps.companies.models import *


class UserRegistrationView(BaseRegistrationView):
    template_name = 'registration/registration_consumer.html'
    form_class = UserCreationForm

    def register(self, request, **cleaned_data):
        email, password = cleaned_data['email'], cleaned_data['password1']
        User.objects.create_user(email, password)

        new_user = authenticate(username=email, password=password)
        login(request, new_user)
        signals.user_registered.send(
            sender=self.__class__,
            user=new_user,
            request=request
            )
        return new_user

    def get_success_url(self, request, user):
        return '/dashboard/'


class CompanyRegistrationView(BaseRegistrationView):
    template_name = 'registration/registration_company.html'
    form_class = CompanyCreationForm

    def register(self, request, **cleaned_data):
        email, password, name = cleaned_data['email'], \
            cleaned_data['password1'], cleaned_data['name']

        User.objects.create_user(email, password)
        print password

        # login the new user
        new_user = authenticate(username=email, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)

        # create the institute and associate it with the newly created user
        company = Company.objects.create(name=name)
        group = CompanyGroup.objects.create(name='Administrators', company=company)
        CompanyUser.objects.create(
            user=new_user, company=company, group=group,
            is_owner=True, is_superuser=True, is_default=True)

        return new_user

    def get_success_url(self, request, user):
        return '/dashboard/'
