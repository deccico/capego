import re

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import EmailField
from django.core.exceptions import ValidationError

from models import NewsletterSubscriber, UsersContactingCapego

def isEmailAddressValid(email):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False

def subscribe(request):
    if request.method == 'POST' and request.POST.get('email'):
        email = request.POST.get('email').lower()
        if not isEmailAddressValid(email):
            msg = "<strong>%s is not a valid email</strong>" % email
        else:
            msg = "<strong>%s </strong> is now subscribed to our newsletter ;)" % email
            s = NewsletterSubscriber(email=email)
            s.save()
        return HttpResponse(msg)


def message(request):
    if request.method == 'POST' and request.POST.get('email'):
        u = UsersContactingCapego(name=request.POST.get('name').lower(), email=request.POST.get('email').lower(), message=request.POST.get('message'))
        u.save()
        msg = """<div class='alert alert-info'>
        <button class='close' data-dismiss='alert'>x</button>
        Your message has been sent successfuly  ;) </div>"""
        return render_to_response('contact.html', {'message': msg}, RequestContext(request))
    else:
        msg = """<div class='alert'>
        <button class='close' data-dismiss='alert'>x</button>
        Your message did not contain valid data or there was an error processing it. </div>"""
        return render_to_response('contact.html', {'message': msg}, RequestContext(request))





