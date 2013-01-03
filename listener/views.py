from django.http import HttpResponse
import json

from models import Listener
import corrector
import formatter

cor = corrector.Corrector()
fmt = formatter.Formatter()

#here the view function starts
def check(request, listener_id, line_id, line):
    return HttpResponse(get_dialog(listener_id, line_id, line))


def get_dialog(listener_id, line_id, line):
    d = Listener.objects.get(id=listener_id).dialog
    good_one = json.loads(d)[int(line_id)][1]
    corrected = cor.correct_dialog(good_one, line)
    formatted = fmt.line_corrected(corrected, line_id)
    return formatted
 
