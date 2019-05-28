import unittest
from app import listpeople


class TestPerson(unittest.TestCase):
    def test_app(self):
        self.assertEqual(listpeople(),'2')