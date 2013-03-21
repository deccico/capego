from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^badges/$', 'user_data.views.user_badges'),
)