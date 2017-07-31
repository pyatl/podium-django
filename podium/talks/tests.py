from datetime import date

from django.test import TestCase

from .models import Session


class SessionTestCase(TestCase):

    def test_get_absolute_url(self):
        Session.objects.create(date=date(2020, 1, 1))
        self.assertEqual(
            Session.objects.get(id=1).get_absolute_url(), '/talks/sessions/1/')
