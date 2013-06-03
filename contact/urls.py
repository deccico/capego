from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from contact.views import message

urlpatterns = patterns('',
                       (r'^$', TemplateView.as_view(template_name="contact/contact.html")),
                       (r'^about/$', TemplateView.as_view(template_name="contact/about.html")),
                       (r'^donate/$', TemplateView.as_view(template_name="contact/donate.html")),
                       url(r'^message/$', message, name='message'),
                       url(r'^subscribe/$', 'contact.views.subscribe'),
)

