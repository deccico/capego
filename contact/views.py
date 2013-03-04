from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import NewsletterSubscriber, UsersContactingCapego


def subscribe(request, email):
    return HttpResponse("all good..")

def message(request):
    if request.method == 'POST' and request.POST.get('email'):
        email = request.POST.get('email')
        message = request.POST.get('message')
        name = request.POST.get('name')
        u = UsersContactingCapego(name=name, email=email, message=message)
        u.save()
        msg = """<div class='alert alert-info'>
        <button class='close' data-dismiss='alert'>x</button>
        Your message has been sent successfuly  ;) </div>"""
        return render_to_response('contact.html', {'message': msg}, RequestContext(request))




