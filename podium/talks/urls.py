from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^submit/', views.submit_talk_view, name='talks-submit'),
]
