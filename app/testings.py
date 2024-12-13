import unittest
import requests


class TestFastApi(unittest.TestCase):
    @unittest.skip("Skipping")
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

    def test_private_view(self):
        headers = {
            "auth": "1"
        }
        r = requests.get("http://127.0.0.1:8000/api/private/", headers=headers)
        print("YE this is workighn")
        self.assertEqual(r.status_code, 200)
