from django.http import HttpResponse
from models import Listener


#here the view function starts
def check(request, listener_id):
    return HttpResponse(getDialog(listener_id))


def getDialog(listener_id):
    l = Listener.objects.get(id=listener_id)
    return l.formatted_dialog
 
