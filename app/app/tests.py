from .calc import add
from django.test import SimpleTestCase

class CalcTests(SimpleTestCase):
    "Test cal module"

    def test_add_numbers(self):
        res = add(5,6)
        self.assertEqual(res, 11)


