from datetime import date

from django.http import Http404
from django.test import Client, TestCase

from .models import Talk, Session
from . import views


class TalkTestCase(TestCase):

    # Model

    def test_get_absolute_url(self):
        Talk.objects.create()
        self.assertEqual(
            Talk.objects.get(id=1).get_absolute_url(), '/talks/talks/1/')


class SessionTestCase(TestCase):

    # Model

    def test_get_absolute_url(self):
        Session.objects.create(date=date(2020, 1, 1))
        self.assertEqual(
            Session.objects.get(id=1).get_absolute_url(), '/talks/sessions/1/')

    # View

    def test_session_talk_list_view(self):
        """Raise the right exception when the session does not exist."""
        self.assertRaises(
            Http404,
            views.session_talk_list_view,
            Client().get('/talks/sessions/1/'), 1)
