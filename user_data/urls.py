from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^badges/$', 'user_data.views.user_badges'),
                       #(r'^badges/$', TemplateView.as_view(template_name="user/badges.html")),
)