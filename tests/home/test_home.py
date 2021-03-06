from tests.helpers import with_client, setUpApp, with_context
import unittest


class TestHome (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_get_api(self, client):
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('"/helloworld"', response.data.decode())
