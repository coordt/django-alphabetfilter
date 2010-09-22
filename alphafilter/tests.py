import unittest
from django.contrib.auth.models import User
from django.template import RequestContext, Context, Template

from django.test import Client
from django.core.handlers.wsgi import WSGIRequest

class RequestFactory(Client):
    """
    Class that lets you create mock Request objects for use in testing.
    
    Usage:
    
    rf = RequestFactory()
    get_request = rf.get('/hello/')
    post_request = rf.post('/submit/', {'foo': 'bar'})
    
    This class re-uses the django.test.client.Client interface, docs here:
    http://www.djangoproject.com/documentation/testing/#the-test-client
    
    Once you have a request object you can pass it to any view function, 
    just as if that view had been hooked up using a URLconf.
    """
    def request(self, **request):
        """
        Similar to parent class, but returns the request object as soon as it
        has created it.
        """
        environ = {
            'HTTP_COOKIE': self.cookies,
            'PATH_INFO': '/',
            'QUERY_STRING': '',
            'REQUEST_METHOD': 'GET',
            'SCRIPT_NAME': '',
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80,
            'SERVER_PROTOCOL': 'HTTP/1.1',
        }
        environ.update(self.defaults)
        environ.update(request)
        return WSGIRequest(environ)


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