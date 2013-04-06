from user_data.models import Activity, UserSolvedListener
from user_data.models import UserActivity
from user_data.models import UserExtraData
from listener.models import Listener



def get_solve_video_key(request, listener_id):
    key =  request.user.username + "-" + str(listener_id)
    return key

def init_listen_record(request, key, len_lines):
    if not request.session.has_key(key):
        request.session[key] = [0] + ([False] * (len_lines))


def mark_line_correct_and_check_if_video_is_correct(request, listener_id, line_id, len_lines, level):
    if not request.user.is_authenticated():
        return
    key = get_solve_video_key(request, listener_id)
    init_listen_record(request, key, len_lines)
    request.session[key][line_id] = True
    if not False in request.session[key][1:]:
        award_badge = award_points_and_decide_if_award_badge(request, key, level)
        UserSolvedListener(user=request.user, listener=Listener.objects.get(id=listener_id), number_of_suggestions=request.session[key][0]).save()
        if award_badge:
            UserActivity(user=request.user, related_activity=Activity.objects.get(name="Solve video"), description=key).save()
        del request.session[key]

def count_suggestion(request, listener_id, len_lines):
    if not request.user.is_authenticated():
        return
    key = get_solve_video_key(request, listener_id)
    init_listen_record(request, key, len_lines)
    request.session[key][0] += 1

def award_points_and_decide_if_award_badge(request, key, level):
    points = level*5 - request.session[key][0]
    u = UserExtraData.objects.get(user=request.user)
    u.points += points
    u.save()
    award_badge =  (float(request.session[key][0]) / points) < 0.5
    return award_badge
