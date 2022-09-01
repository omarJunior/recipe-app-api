from .calc import (
    add,
    substract,
)
from django.test import SimpleTestCase

class CalcTests(SimpleTestCase):
    "Test cal module"

    def test_add_numbers(self):
        """ Test Adding numbers """
        res = add(5,6)
        self.assertEqual(res, 11)


    def test_substract_numbers(self):
        "Test substracting numers"
        res = substract(10,15)
        self.assertEqual(res, 5)

