from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from user_data.models import UsersBadge


@login_required
def user_badges(request):
    user_badges = UsersBadge.objects.filter(user=request.user).order_by('badge.id').order_by('-award_date')
    return render_to_response('user/badges.html', user_badges)

