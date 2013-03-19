from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from user_data.models import UsersBadge


@login_required
def user_badges(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('user')

    user_badges = UsersBadge.objects.filter(user=request.user).order_by('badge.id').order_by('-award_date')
    return render_to_response('/user/badges.html', user_badges)
    # url(r'^badges$',
    #     ListView.as_view(
    #         queryset=UsersBadge.objects.get().order_by('-award_date'),
    #         context_object_name='user_badges',
    #         template_name='user/badges.html')),
    #return render_to_response('user/badges.html', {'version': version},
    #                          RequestContext(request))
