from django.http import HttpResponse
from django.conf import settings 
import urllib
import urllib2
import json
from django.shortcuts import render


def validate_captcha(view):
    '''Decorator to validate a captcha based on settings'''

    def wrap(request, *args, **kwargs):

        def failure():
            return render(request, 'captcha_fail.html',)

        if request.method == 'POST':

            url = "https://www.google.com/recaptcha/api/siteverify"
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': request.POST.get(u'g-recaptcha-response', None),
                'remoteip': request.META.get("REMOTE_ADDR", None),
            }

            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = json.loads(response.read())

            # result["success"] will be True on a success
            if result["success"]:
                return view(request, *args, **kwargs)
            else:
                return failure()
        return view(request, *args, **kwargs)
    return wrap