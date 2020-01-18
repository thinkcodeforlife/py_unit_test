import unittest
from myapp import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)

