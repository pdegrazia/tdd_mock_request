import unittest
from unittest.mock import patch
from mymodule import RequestClass, MainClass


class MockRequestTest(unittest.TestCase):
    @patch('mymodule.RequestClass')
    def test_post_request(self, MockRequestClass):
        mock_request = MockRequestClass()

        mock_request.post_request.return_value = {'access_token': 'some_access_token'}
        mock_request.post_request.ok = True

        response = mock_request.post_request()

        self.assertTrue(isinstance(response, dict))
        self.assertTrue(response['access_token'] == 'some_access_token')


class MainClassTest(unittest.TestCase):
    @patch('mymodule.RequestClass')
    def test_request(self, mock_request):
        mock_request.post_request.return_value = {'access_token': 'some_access_token'}
g
        mc = MainClass()
        call = mc.make_call()

        self.assertTrue('access_token' in call.keys())
