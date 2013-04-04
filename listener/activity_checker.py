from django.contrib.auth.models import User

class ActivityChecker():
    def check_video_correct(self, is_correct, request, listener_id, line_id, len_lines):
        if not is_correct:
            return
        #check if logged in
        if not request.user.is_authenticated():
            return
        #get key
        key = request.user.username + "-" + str(listener_id)
        #create session variable if necessary
        if not request.session.has_key(key):
            request.session[key] = "F" * len_lines
        #change subindex
        #check if ok
        #award price
        request.session['has_commented'] = True