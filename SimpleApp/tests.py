"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from hamcrest import *
from django.test.client import Client
from django.test import TestCase


__author__ = 'tdd'

class SystemTests(TestCase):
    def test_get_html_message(self):
        client = Client()
        response = client.get('/html_message/')
        self.assertEqual(200, response.status_code)
        assert_that(response.content,
                    contains_string("Hello"))
        