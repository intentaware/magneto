from django.conf.urls import patterns, url
from .views import DashboardView, AngularPartials

urlpatterns = patterns(
    '',
    url(r'^$',
        DashboardView.as_view(),
        name='dashboard'),
    url(
        r'partials/(?P<template_name>.+\.html?$)',
        AngularPartials.as_view(), name='partials'
    ),
)
