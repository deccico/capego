from django.http import HttpResponse

from models import Listener
import corrector
import formatter

cor = corrector.Corrector()
fmt = formatter.Formatter()

def check(request, listener_id, line_id, line):
    good_one = Listener.get_good_line(listener_id, line_id)
    is_correct,corrected_dialog = cor.correct_dialog(good_one, line)
    formatted = fmt.line_corrected(is_correct, corrected_dialog, line_id, listener_id)
    return HttpResponse(formatted)

def get_next_word(request, listener_id, line_id, line):
    good_one = Listener.get_good_line(listener_id, line_id)
    is_correct,corrected_dialog = cor.get_next_word(good_one, line)
    formatted = fmt.line_corrected(is_correct, corrected_dialog, line_id, listener_id)
    return HttpResponse(formatted)

