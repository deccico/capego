from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       (r'^$', direct_to_template, {'template': 'contact.html'}),
                       (r'^about/$', direct_to_template, {'template': 'about.html'}),
)

