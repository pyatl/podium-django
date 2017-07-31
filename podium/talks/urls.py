from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.session_list_view, name='talks-index'),
    url(r'^submit/$', views.submit_talk_view, name='talks-submit'),
    url(r'^sessions/$', views.session_list_view, name='talks-sessions'),
    url(r'^sessions/(\d+)/$', views.session_talk_list_view,
        name='talks-sessions-id')
]
