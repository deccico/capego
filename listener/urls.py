from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from listener.models import Listener

urlpatterns = patterns('',
    url(r'^$',
       ListView.as_view(
           queryset=Listener.objects.order_by('-update_date')[:10],
           context_object_name='latest_listener_list',
           template_name='listener/index.html')),
    url(r'^(?P<pk>\d+)/$',
       DetailView.as_view(
           model=Listener,
           template_name='listener/video_play.html')),
    url(r'^check/(?P<listener_id>\d+)/line_id(?P<line_id>\d+)/(?P<line>.+)/$', 'listener.views.check'),
)

