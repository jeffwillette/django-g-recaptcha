import unittest
import os
from django.test.client import RequestFactory
from django.http import HttpResponse
from django.test import TestCase
from mock import patch
from validate_recaptcha import validate_captcha
from mock import MagicMock, patch

@validate_captcha
def foo_view(request):
	"""Dummy view that I will wrap"""
	return HttpResponse("it worked")

class CaptchaTest(TestCase):

	def setUp(self):
		"""Setting up what I need for the test"""
		self.rf = RequestFactory()

	@patch('json.loads')
	@patch('urllib2.urlopen')
	def test_validate_captcha_http(self, urlopen_mock, loads_mock):
		"""making a function wrapped, testing return http"""
		loads_mock.return_value = {"success": False}
		request = self.rf.post('', {})
		#x = validate_captcha(self.foo_view(request))
		x = foo_view(request)
		self.assertTrue(x.status_code == 401)

	@patch('json.loads')
	@patch('urllib2.urlopen')
	def test_validate_captcha_ajax(self, urlopen_mock, loads_mock):
		"""making a function wrapped, testing return ajax"""
		loads_mock.return_value = {"success": False}
		request = self.rf.post('', {}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		self.assertTrue(request.is_ajax())
		#x = validate_captcha(self.foo_view(request))
		x = foo_view(request)
		self.assertTrue(x.status_code == 401)

	@patch('json.loads')
	@patch('urllib2.urlopen')
	def test_validate_captcha_pass(self, urlopen_mock, loads_mock):
		"""making a function wrapped, testing return dict['success']"""

		request = self.rf.post('',
			{'g-recaptcha-response': None,
			 'REMOTE_ADDR': None})

		bar = foo_view(request)
		urlopen_mock.assert_called()
		loads_mock.assert_called()

	def test_original_func(self):
		"""Testing that the call to the bare function works"""
		test = foo_view
		self.assertTrue(test.func_name == "wrap")
		test = foo_view._original
		self.assertTrue(test.func_name == "foo_view")

	def test_get_validate_captcha_wrapped(self):
		"""Testing that the get request to the wrapper just returns the view"""
		request = self.rf.get('')
		test = foo_view(request)
		self.assertEqual(test.content, 'it worked')
