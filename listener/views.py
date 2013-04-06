from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.html import strip_tags

from models import Listener
import activity_checker

import corrector
import formatter

cor = corrector.Corrector()
fmt = formatter.Formatter()

def check(request, listener_id, line_id, line):
    good_one, len_lines, level = Listener.get_good_line(listener_id, line_id)
    is_correct, corrected_dialog = cor.correct_dialog(strip_tags(good_one), strip_tags(line))
    formatted = fmt.line_corrected(is_correct, corrected_dialog, line_id, listener_id)
    if is_correct:
        #len_lines is +1 since first entry is for suggestions
        activity_checker.mark_line_correct_and_check_if_video_is_correct(request, listener_id, int(line_id), len_lines + 1, level)
    return HttpResponse(formatted)

def get_next_word(request, listener_id, line_id, line):
    good_one, len_lines, level = Listener.get_good_line(listener_id, line_id)
    is_correct, corrected_dialog = cor.get_next_word(strip_tags(good_one), strip_tags(line))
    formatted = fmt.line_corrected(is_correct, corrected_dialog, line_id, listener_id)
    activity_checker.count_suggestion(request, listener_id, len_lines)
    return HttpResponse(formatted)

def play(request, listener_id):
    l = Listener.objects.get(id=listener_id)
    good_one, len_lines, level = Listener.get_good_line(listener_id, 0)
    activity_checker.clean_solve_video_entry(request, l.id, len_lines)
    return render_to_response('listener/play.html', {'listener': l}, RequestContext(request))

