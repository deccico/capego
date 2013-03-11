from django.conf.urls import patterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       (r'^badges/$', TemplateView.as_view(template_name="user/badges.html")),
)



