import unittest
from app import app

class TestSearch(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_search(self):
        response = self.app.get('/search?q=mario')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Super Mario World', response.data)
