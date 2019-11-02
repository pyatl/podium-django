from django.conf.urls import url
from pyatl.views import (
    LandingPageView,
    EventView,
    EventsView,
    LocationView,
    LocationsView,
    PageView,
    EventInviteDownloadView,
)

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing-page'),

    # page
     url(r'^(?P<slug>[-\w\d]+)/(?P<pk>[0-9]+)/$', PageView.as_view(), name='page'),

    # event
    url(r'^event/(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/(?P<slug>[-\w\d]+)/(?P<pk>[0-9]+)/$', EventView.as_view(), name='event'),
    url(r'^event/invite/(?P<pk>[0-9]+)/$', EventInviteDownloadView.as_view(), name='event-invite'),
    url(r'^events/$', EventsView.as_view(), name='events'),

    # location
    url(r'^location/(?P<slug>[-\w\d]+)/(?P<pk>[0-9]+)/$', LocationView.as_view(), name='location'),
    url(r'^locations/$', LocationsView.as_view(), name='locations'),
]
