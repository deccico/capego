from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from app.views import home, done, logout, error, form, form2, close_login_popup
from app.facebook import facebook_view


admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^listen/', include('listener.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('listener.urls')),
    url(r'^index\.html/', include('listener.urls')),
    (r'^contact/$', direct_to_template, {'template': 'contact.html'}),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),

    url(r'^fb/', facebook_view, name='fb_app'),
    url(r'', include('social_auth.urls')),
)
