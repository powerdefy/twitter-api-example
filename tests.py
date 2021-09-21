import os
import json
import unittest
from app import app


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()
        print("In method", self._testMethodName)

    # executed after each test
    def tearDown(self):
        pass


###################
#### test case ####
###################


    def test_hashtags_search_page(self):
        response = self.app.get('/hashtags/python?limit=10',)
        self.assertEqual(response.status_code, 200)

        response_count = json.loads(response.data).get(
            "search_metadata").get("count")
        self.assertEqual(response_count, 10)

    def test_user_timeline(self):
        response = self.app.get('/users/twitterapi?limit=10')
        self.assertEqual(response.status_code, 200)

        response_count = len(json.loads(response.data))
        self.assertEqual(response_count, 10)


if __name__ == "__main__":
    unittest.main()
