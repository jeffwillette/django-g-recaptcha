import unittest
import os
from django.test.client import RequestFactory
from validate_recaptcha import validate_captcha

class CaptchaTest(unittest.TestCase):

	def setUp(self):
		"""Setting up what I need for the test"""
		self.rf = RequestFactory()

	def foo_view(self, request):
		"""Dummy view that I will wrap"""
		return 'foo'

	def test_validate_captcha(self):
		"""making a function wrapped"""
		request = self.rf.post('', {})
		x = validate_captcha(self.foo_view(request))
		x = x(request)
		self.assertTrue(x.status_code == 401)
