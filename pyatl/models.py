from django.db import models
from tinymce import models as tinymce_models
from ics import Calendar
from ics import Event as CalendarEvent


class Location(models.Model):
    '''
    Defines an event's location.
    For physycal locations it allows
    for optional open street maps embed codes
    in the field map_embed_code.
    This is an iframe embed code provided
    in the open street maps website.

    For online locations, simply leave the map_embed_code
    field blank and include a link to the online room
    in the description.
    '''
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = tinymce_models.HTMLField()
    map_embed_code = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    '''
    Defines a group event.

    short_description: Tweet sized event description
    '''
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    short_description = models.TextField(max_length=280)
    description = tinymce_models.HTMLField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    published = models.BooleanField(default=False)
    location = models.ForeignKey('Location', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    @property
    def slugify_start(self):
        '''
        Event.start.date as slug
        '''
        return self.start.strftime('%Y-%m-%d')

    class Meta:
        ordering = ['start']


class Page(models.Model):
    '''
    Defines a generic content page.
    Meant for content like the Code of Conduct.

    Field footer_link defines if a link to this page
    should be included in the footer area.
    '''
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = tinymce_models.HTMLField()
    published = models.BooleanField(default=False)
    footer_link = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class EventInvite(object):
    '''
    Creates a ics calendar invite for people to
    download from site.
    '''

    def __init__(self, event, host, scheme):
        '''
        :param event: Event object
        :param host: HTTP Host str
        :param scheme: http or https str
        '''
        self._event = event
        self._host = host
        self._scheme = scheme

    def generate(self):
        '''
        Generates the ics calendar invite
        '''
        calendar = Calendar()
        calendar_event = CalendarEvent()
        calendar_event.begin = self._event.start
        calendar_event.end = self._event.end
        calendar_event.name = self._event.name
        calendar_event.description = self._description()
        calendar_event.url = self._url()
        calendar_event.location = self._location()
        calendar.events.add(calendar_event)
        return calendar

    def _url(self):
        '''
        Event url in pyatl site.
        '''
        return '{0}://{1}/event/{2}/{3}/{4}/'.format(
            self._scheme,
            self._host,
            self._event.slugify_start,
            self._event.slug,
            self._event.pk
            )

    def _location(self):
        '''
        The event location name and a link
        to the location's page on pyatl site.
        '''
        return '{0} - {1}://{2}/location/{3}/{4}/'.format(
            self._event.location.name,
            self._scheme,
            self._host,
            self._event.location.slug,
            self._event.location.pk
            )

    def _description(self):
        '''
        The event description.
        Includes a link to the event page
        and a lino to the location.
        '''
        return '{0} \n Learn more at: {1} \n Event Location: {2}'.format(
            self._event.short_description,
            self._url(),
            self._location()
            )
