# Change.md #

## Modified: ##

-**podium/settings.py**
-*Add "crispy_forms" to "INSTALLED_APPS" in settings.py*
-*Add "registration" to "INSTALLED_APPS" in settings.py*
-*Add "CRISPY_TEMPLATE_PACK ='bootstrap3'" Key/value to settings.py*
-*Add "url(r'^accounts/', include('registration.backends.default.urls'))," to podium.urls.py*

-**podium/talks/models.py**
-*Add  "__str__" methods*

-**podium/talks/templates/talks/submit.html**
-*Add "crispy" template tag /form tag*

-**requirements.txt**
-*Add "django-crispy-forms1.6.1"*
-*Add "django-registration-redux 1.6"*
    
## New files: ##

-**templates/base.html**
-*Move "base.html" to project folder*

-**templates/head.htm**
-*Include "head"  in base.*

-**templates/js.htm**
-*Include "script"  in base.*

-**templates/nav.htm** 
-*Include "nav.htm" in base.* 

-**templates/style.htm**
-*Include "style.htm"(to be moved to seperate style sheet when complete.) in base.*

## Deleted: ##    

-**podium/talks/templates/base.html**
-*Move to project level "podium-django/templates/base.html"
to improve plug/play aspect of Talks app.*
