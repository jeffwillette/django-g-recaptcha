from django.http import HttpResponse
from django.conf import settings 
import urllib
import urllib2
import json
from django.shortcuts import render




def validate_captcha(view):
    '''Decorator to validate a captcha based on settings
    --validate captcha also has some special html to populate the G-Recaptcha site key from context processors /main/contact.html
    --There is also some jquery to handle it asynchronously in static/main/mainscript
    --Also need to put the g-script for the g-recaptcha div to load'''

    def wrap(request, *args, **kwargs):

        def failure_http():
            return render(request, 'captcha_fail.html',)

        def failure_ajax():
            return HttpResponse('There was a problem with the captcha, please try again')

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
            elif request.is_ajax():
                return failure_ajax()
            else:
                return failure_http()

        return view(request, *args, **kwargs)
    return wrap