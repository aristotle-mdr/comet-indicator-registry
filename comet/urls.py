from django.conf.urls import include, patterns, url

from comet import views#,forms
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('comet.views',
    url(r'^/?$', TemplateView.as_view(template_name='comet/static/about_comet_mdr.html')),
    url(r'^indicator/(?P<iid>\d+)?/?$', views.indicator, name='indicator'),
    url(r'^qualitystatement/(?P<iid>\d+)/?$', views.qualitystatement, name='qualitystatement'),
    url(r'^datasource/(?P<iid>\d+)/?$', views.datasource, name='datasource'),

#These are required for about pages to work. Include them, or custom items will die!
    url(r'^about/(?P<template>.+)/?$', views.DynamicTemplateView.as_view(), name="about"),
    url(r'^about/?$', TemplateView.as_view(template_name='comet/static/about_comet_mdr.html'), name="about"),
)

