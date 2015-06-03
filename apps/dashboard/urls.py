from django.conf.urls import patterns, url
from .views import DashboardView, AngularPartials, user_opt_out

urlpatterns = patterns('',
    url(r'^$', DashboardView.as_view(),name='dashboard'),
    url(r'partials/(?P<template_name>.+\.html?$)',AngularPartials.as_view(), name='partials'),
    url(r'^optout/', user_opt_out),
)
