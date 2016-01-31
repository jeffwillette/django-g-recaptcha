# GOOGLE RECAPTCHA DJANGO DECORATOR #

* A decorator, which can be used on django views to validate google-recatpcha forms
* Version 0.1

# SETUP #

## 1. Download and install ## 
```
#!python

pip install django-g-recaptcha
```
 
## 2. Add.. ##
```
#!python

GOOGLE_RECAPTCHA_SITE_KEY = 'key_obtained_from_google'
GOOGLE_RECAPTCHA_SECRET_KEY = 'key_obtained_from_google' 
```
to your settings.py file

## 3. Pass the site key in your context... ##

```
#!python

from django.conf import settings
def view(request):

context = {
    'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY,
}

return render(request, 'template.html', context)
```

## 4. Add the google recaptcha script to your <head> ##

## 5. Add the recaptcha div with the site key passed in your context... ##

```
#!html


<div class="g-recaptcha" data-sitekey="{{ GOOGLE_RECAPTCHA_SITE_KEY }}"></div>
```
## 6. add the decorator to your views... ##


```
#!python

@validate_captcha
def view(request):
    ...
```
## 7. Add g_recaptcha to your installed apps ... ##


```
#!python

INSTALLED_APPS += ('g_recaptcha')
```
On a successful captcha submission it will process the rest of the view, if it fails, it will render a template which says there was a problem with the captcha. Override or extend this template however you see fit.