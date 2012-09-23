from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'capego.views.home', name='home'),
    # url(r'^capego/', include('capego.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
