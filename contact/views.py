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
            if NewsletterSubscriber.objects.filter(email=email).count() > 0:
                msg = "<strong>%s </strong> was already subscribed to our newsletter." % email
            else:
                try:
                    s = NewsletterSubscriber(email=email)
                    s.save()
                except:
                    msg = "<strong>There was an error subscribing %s. </br>Please notify the problem to info@capego.com</strong>" % email
        return HttpResponse(msg)


def message(request):
    if request.method == 'POST' and request.POST.get('email'):
        email = request.POST.get('email').lower()
        #add this when the form in the error doesn't get erased
        # if not isEmailAddressValid(email):
        #     result = "<strong>%s is not a valid email</strong>" % email
        #     msg = """<div class='alert alert-error'>
        #     <button class='close' data-dismiss='alert'>x</button>
        #     %s  </div>""" % result
        # else:
        u = UsersContactingCapego(name=request.POST.get('name').lower(), email=email, message=request.POST.get('message'))
        u.save()
        msg = """<div class='alert alert-info'>
        <button class='close' data-dismiss='alert'>x</button>
        Your message has been sent successfuly  ;) </div>"""
        return render_to_response('contact/contact.html', {'message': msg}, RequestContext(request))
    else:
        msg = """<div class='alert'>
        <button class='close' data-dismiss='alert'>x</button>
        Your message did not contain valid data or there was an error processing it. </div>"""
        return render_to_response('contact/contact.html', {'message': msg}, RequestContext(request))

