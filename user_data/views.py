import json

from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from user_data.models import UserBadge, Badge, UserActivity, Activity
from django.conf import settings

import logging
logger = logging.getLogger(settings.APP_NAME)

@login_required
def user_badges(request):
    user_badges = UserBadge.objects.filter(user=request.user)
    ub_ids = []
    for ub in user_badges:
        ub_ids.append(ub.badge.id)
    badges = Badge.objects.all().order_by('name')
    for b in badges:
        b.awarded = b.id in ub_ids
    return render_to_response('user/badges.html', {'badges': badges}, RequestContext(request))

@login_required
@transaction.commit_on_success
def register_activity(request):
    if not request.method == 'POST' or not request.POST.get('activity_code'):
        return
    try:
        activity_code = int(request.POST.get('activity_code'))
    except ValueError:
        logger.exception("%s is not an integer" % request.POST.get('activity_code'))
        return

    usr = request.user
    desc = request.POST.get('description') if request.POST.get('description') else ""

    status = True
    try:
        #todo: we should have a transaction here for the whole request
        ua = UserActivity(user=usr, related_activity=Activity.objects.get(id=activity_code), description=desc)
        ua.save()
    except IntegrityError:
        msg = "OK. Trying to record activity: user:%s, activity:%s, desc:%s but seems to be duplicated, which is as designed." % (usr, activity_code, desc)
        status = False
        logger.debug(msg)
    except:
        status = False
        msg = "Error recording activity: user:%s, activity:%s, desc:%s but seems to be duplicated, which is as designed." % (usr, activity_code, desc)
        logger.exception(msg)

    #this message will notify success on the operation and help whether JS should keep sending them
    out = [{'status':status,'event_key':usr.username + str(activity_code) + desc.replace(" ", "") }]
    return HttpResponse(json.dumps(out))
