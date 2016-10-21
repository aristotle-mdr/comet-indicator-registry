from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('aristotle_mdr.urls')),
    url(r'^comet/', include('comet.urls',app_name="comet",namespace="comet")),
    )