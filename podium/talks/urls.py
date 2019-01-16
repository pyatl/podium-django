from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.session_list_view, name='talks-index'),
    url(r'^submit/$', views.submit_talk_view, name='talks-submit'),
    url(r'^sessions/$', views.session_list_view, name='talks-sessions'),
    url(r'^sessions/(?P<date>\d{4}-\d{2}-\d{2})/$',
        views.session_talk_list_view,
        name='talks-sessions-id'),
    url(r'^talks/(?P<slug>[\w-]+)/$',
        views.talk_detail_view, name='talks-talk-id'),
    url(r'^talks/$', views.talk_list_view, name='talk-list'),
]
