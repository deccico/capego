from django.conf.urls.defaults import patterns, url, include
from auth.views import home, user, logout, error, form, form2, close_login_popup
from auth.facebook import facebook_view

urlpatterns = patterns('',
                       url(r'^$', home, name='home'),
                       url(r'^user/$', user, name='user'),
                       url(r'^error/$', error, name='error'),
                       url(r'^logout/$', logout, name='logout'),
                       url(r'^form/$', form, name='form'),
                       url(r'^form2/$', form2, name='form2'),
                       url(r'^fb/', facebook_view, name='fb_app'),
                       url(r'^close_login_popup/$', close_login_popup, name='login_popup_close'),
                       url(r'', include('social_auth.urls')),
                       )
