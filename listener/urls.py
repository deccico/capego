from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from listener.models import Listener

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Listener.objects.order_by('-update_date')[:5],
            context_object_name='latest_listener_list',
            template_name='listener/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Listener,
            template_name='listener/video_play.html')),
    #test display of static resources
    url(r'^test/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Listener,
            template_name='listener/detail.html')),
    url(r'^check/(?P<listener_id>\d+)/$', 'listener.views.check'),
)

