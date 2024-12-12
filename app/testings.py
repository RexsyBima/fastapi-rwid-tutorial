import unittest
import requests


class TestFastApi(unittest.TestCase):
    def test_route(self):
        data = {
            "id": 0,
            "title": "string",
            "is_important": True,
            "is_completed": False,
            "date": "2024-12-05T07:44:05.626Z"
        }

        r = requests.post("http://127.0.0.1:8000/api/create/todo/", json=data)
        self.assertEqual(r.status_code, 201)
