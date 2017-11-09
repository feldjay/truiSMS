import unittest
import app


class TestSMS(unittest.TestCase):

    def test_sms(self):
        self.test_app = app.app.test_client()

        response = self.test_app.post('/sms', data={'From': '+15556667777'})

        self.assertEquals(response.status, "200 OK")
