from django.conf.urls import patterns, url
from .views import DashboardView, AngularPartials

urlpatterns = patterns(
    'dashboard',
    url(
        r'^$', DashboardView.as_view(), name='main'
    ),
    url(
        r'partials/(?P<template_name>.+\.html?$)',
        AngularPartials.as_view(), name='partials'
    ),
)
