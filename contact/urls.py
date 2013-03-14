from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from contact.views import message

urlpatterns = patterns('',
                       (r'^faq$', TemplateView.as_view(template_name="contact/faq.html")),
                       (r'^about/$', TemplateView.as_view(template_name="contact/about.html")),
                       url(r'^message/$', message, name='message'),
                       url(r'^subscribe/$', 'contact.views.subscribe'),
)

