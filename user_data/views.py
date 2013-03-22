from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from user_data.models import UsersBadge


@login_required
def user_badges(request):
    user_badges = UsersBadge.objects.filter(user=request.user).order_by('-badge','-award_date')
    return render_to_response('user/badges.html', {'user_badges': user_badges}, RequestContext(request))

