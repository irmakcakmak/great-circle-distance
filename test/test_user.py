import unittest

from user import User


class UserTest(unittest.TestCase):

    def test_less_than_comparison(self):
        user1 = User(1, "user1")
        user2 = User(2, "user2")
        self.assertLess(user1, user2)

    def test_malformed_data(self):
        with self.assertRaises(ValueError):
            User.from_record({"id": 1, "names": "malformed"})
