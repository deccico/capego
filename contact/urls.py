from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template

from contact.views import message

urlpatterns = patterns('',
                       (r'^$', direct_to_template, {'template': 'contact.html'}),
                       (r'^about/$', direct_to_template, {'template': 'about.html'}),
                       url(r'^message/$', message, name='message'),
                       url(r'^subscribe/$', 'contact.views.subscribe'),
)

