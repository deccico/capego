from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from user_data.models import UsersBadge, Badge


@login_required
def user_badges(request):
    user_badges = UsersBadge.objects.filter(user=request.user)
    ub_ids = []
    for ub in user_badges:
        ub_ids.append(ub.badge.id)
    badges = Badge.objects.all().order_by('name')
    for b in badges:
        b.awarded = b.id in ub_ids
    return render_to_response('user/badges.html', {'badges': badges}, RequestContext(request))

