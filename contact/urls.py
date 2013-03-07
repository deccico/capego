from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from contact.views import message

urlpatterns = patterns('',
                       (r'^$', TemplateView.as_view(template_name="contact.html")),
                       (r'^about/$', TemplateView.as_view(template_name="about.html")),
                       url(r'^message/$', message, name='message'),
                       url(r'^subscribe/$', 'contact.views.subscribe'),
)

