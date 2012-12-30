from django.http import HttpResponse
from models import Listener


#here the view function starts
def check(request, listener_id, line_id):
    return HttpResponse(get_dialog(listener_id, line_id))


def get_dialog(listener_id, line_id):
    #l = Listener.objects.get(id=listener_id)
    return "l.dialog_corrected %s %s" % (listener_id, line_id)
 
