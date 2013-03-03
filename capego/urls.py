from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^auth/', include('auth.urls')),
    url(r'^listen/', include('listener.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('listener.urls')),
    url(r'^index\.html/', include('listener.urls')),
    url(r'^contact/', include('contact.urls')),
)
