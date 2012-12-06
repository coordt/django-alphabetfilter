import unittest
from django.contrib.auth.models import User
from django.template import Context, Template

from django.test import Client
from django.core.handlers.wsgi import WSGIRequest
from django.test.client import RequestFactory


class AlphaFilterTestCase(unittest.TestCase):
    def setUp(self):
        usr = User.objects.create_user('sample1', 's@e.org', 'asdf')
        usr.first_name = 'Joe'
        usr.last_name = 'Garfunkel'
        usr.save()

    def tearDown(self):
        User.objects.all().delete()

    def testQSAlphaFilter(self):
        from django.conf import settings
        settings.DEFAULT_ALPHABET = ''
        tmpl = Template('{% load alphafilter %}{% qs_alphabet_filter objects last_name alphafilter/test.html %}')
        ctxt = Context({'objects': User.objects.all()})
        out = tmpl.render(ctxt)
        expected = '[+AAll][+G]'
        self.assertEquals(out, expected)

    def testQSAlphaFilterRequest(self):
        from django.conf import settings
        settings.DEFAULT_ALPHABET = ''
        tmpl = Template('{% load alphafilter %}{% qs_alphabet_filter objects last_name alphafilter/test.html %}')
        req_factory = RequestFactory()
        request = req_factory.get('/?last_name__istartswith=G')

        ctxt = Context({'objects': User.objects.all(), 'request': request})
        out = tmpl.render(ctxt)

        expected = '[+All][+AG]'
        self.assertEquals(out, expected)
