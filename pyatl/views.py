from datetime import timedelta
from ics import Calendar
from ics import Event as CalendarEvent
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404
from pyatl.models import Event, Location, Page


def footer_links(context):
    '''
    Helper function to add footer links
    to views.
    :param context: django response context
    :param type: dict
    '''
    context['page_footer_links'] = Page.objects.filter(
        published=True, footer_link=True)
    return context


class LandingPageView(TemplateView):
    ''' Index page '''
    template_name = 'landing-page.html'

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(
            published=True)[:3] # 3 upcoming events
        context = footer_links(context)
        return context


class EventView(TemplateView):
    ''' Show single Event '''
    template_name = 'event-detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=kwargs['pk'], published=True)
        context = footer_links(context)
        return context


class EventDownloadCalendarInviteView(View):
    '''
    Allows user to download a calendaxr invite
    for an event.
    '''

    def get(self, request, **kwargs):
        '''
        Generates the ical (ics) invite
        for users to download.
        '''
        event = get_object_or_404(Event, pk=kwargs['pk'], published=True)
        end_datetime = event.date + timedelta(hours=2)

        calendar = Calendar()
        calendar_event = CalendarEvent()

        calendar_event.name = event.name
        calendar_event.begin = event.date.strftime('%Y-%m-%d %I:%m:%s')
        calendar_event.end = end_datetime.strftime('%Y-%m-%d %I:%m:%s')
        calendar_event.url = '{0}/event/{1}/{2}/{3}'.format(
            request.META.get('HTTP_HOST'),
            event.slugify_date,
            event.slug,
            event.pk)
        calendar_event.location = '{0} - {1}/location/{2}/{3}'.format(
            event.location.name,
            request.META.get('HTTP_HOST'),
            event.location.slug,
            event.location.pk)
        calendar_event.description = event.short_description

        calendar.events.add(calendar_event)
        response = HttpResponse(calendar, content_type='text/calendar')
        response['Filename'] = '{0}-{1}.ics'.format(event.slug, event.slugify_date)
        response['Content-Disposition'] = 'attachment; filename={0}-{1}.ics'.format(
            event.slug, event.slugify_date)
        return response


class EventsView(TemplateView):
    ''' List all Events '''
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(published=True)
        context['page_footer_links'] = Page.objects.filter(
            published=True, footer_link=True)
        context = footer_links(context)
        return context


class LocationView(TemplateView):
    ''' Show single Location '''
    template_name = 'location-detail.html'

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['location'] = get_object_or_404(Location, pk=kwargs['pk'])
        context = footer_links(context)
        return context


class LocationsView(TemplateView):
    ''' List all Locations '''
    template_name = 'locations.html'

    def get_context_data(self, **kwargs):
        context = super(LocationsView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        context = footer_links(context)
        return context


class PageView(TemplateView):
    ''' Show single Page '''
    template_name = 'page-detail.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(Page, pk=kwargs['pk'])
        context = footer_links(context)
        return context
