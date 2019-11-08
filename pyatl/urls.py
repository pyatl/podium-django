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

slug = '(?P<slug>[-\w\d]+)'
pk = '(?P<pk>[0-9]+)'
date = '(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})'

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing-page'),

    # page
    url(r'^{slug}/{pk}/$'.format(
        slug=slug,
        pk=pk),
        PageView.as_view(),
        name='page'),

    # event
    url(r'^event/{date}/{slug}/{pk}/$'.format(
        date=date,
        slug=slug,
        pk=pk),
        EventView.as_view(),
        name='event'),
    url(r'^event/invite/{pk}/$'.format(
        pk=pk),
        EventInviteDownloadView.as_view(),
        name='event-invite'),
    url(r'^events/$', EventsView.as_view(), name='events'),

    # location
    url(r'^location/{slug}/{pk}/$'.format(
        slug=slug,
        pk=pk),
        LocationView.as_view(),
        name='location'),
    url(r'^locations/$', LocationsView.as_view(), name='locations'),
]
