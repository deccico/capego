from user_data.models import Activity, UserSolvedListener
from user_data.models import UserActivity
from user_data.models import UserExtraData
from listener.models import Listener



def get_solve_video_key(request, listener_id):
    key =  request.user.username + "-" + str(listener_id)
    return key

def get_solve_video_record(request, key, len_lines):
    if not request.session.has_key(key):
        request.session[key] = [0] + ([False] * (len_lines-1))
    return request.session[key]


def mark_line_correct_and_check_if_video_is_correct(request, listener_id, line_id, len_lines, level):
    if not request.user.is_authenticated():
        return
    key = get_solve_video_key(request, listener_id)
    r = get_solve_video_record(request, key, len_lines)
    r[line_id] = True
    if not False in r[1:]:
        award_badge = award_points_and_decide_if_award_badge(request.user, r, level)
        UserSolvedListener(user=request.user, listener=Listener.objects.get(id=listener_id), number_of_suggestions=r[0]).save()
        if award_badge:
            UserActivity(user=request.user, related_activity=Activity.objects.get(name="Solve video"), description=key).save()

def clean_solve_video_entry(request, listener_id, len_lines):
    if not request.user.is_authenticated():
        return
    key = get_solve_video_key(request, listener_id)
    del request.session[key]

def count_suggestion(request, listener_id, len_lines):
    if not request.user.is_authenticated():
        return
    key = get_solve_video_key(request, listener_id)
    r = get_solve_video_record(request, key, len_lines)
    r[0] += 1

def award_points_and_decide_if_award_badge(user, record, listener_id, level):
    points = level*3 - record[0]
    u = UserExtraData.objects.get(user=user)
    u.points += points
    u.save()
    if (level == 3):
        points += 1
    award_badge =  (float(record[0]) / points) < 0.4
    return award_badge
