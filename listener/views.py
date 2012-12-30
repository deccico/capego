from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from models import Listener

line_field = "line"

#here the view function starts
def check(request, listener_id, line_id, line):
    return HttpResponse(get_dialog(listener_id, line_id, line))


def get_dialog(listener_id, line_id, line):
    l = Listener.objects.get(id=listener_id)
    return "corrected %s" % (l)
 
