from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^auth/', include('auth.urls')),
    url(r'^listen/', include('listener.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('listener.urls')),
    url(r'^index\.html/', include('listener.urls')),
    (r'^contact/$', direct_to_template, {'template': 'contact.html'}),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
)
