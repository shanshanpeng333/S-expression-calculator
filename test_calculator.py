from unittest import TestCase
from calculator import calculate


class TestCalculator(TestCase):

    def test_calculator_two_elements(self):
        self.assertEqual(12, calculate("12"))
        self.assertEqual(24, calculate("(add 12 12)"))
        self.assertEqual(37, calculate("(add 12 25)"))
        self.assertEqual(6, calculate("(multiply 2 3)"))
        self.assertEqual(15, calculate("(multiply (add 2 3) 3)"))
        self.assertEqual(18, calculate("(multiply (multiply 2 3) 3)"))
        self.assertEqual(8, calculate("(add (add 2 3) 3)"))
        self.assertEqual(9, calculate("(add (multiply 2 3) 3)"))
        self.assertEqual(26, calculate("(add (multiply 2 3) (multiply 4 5))"))
        self.assertEqual(25, calculate("(add (add 2 3) (multiply 4 5))"))
        self.assertEqual(14, calculate("(add (add 2 3) (add 4 5))"))
        self.assertEqual(45, calculate("(multiply (add 2 3) (add 4 5))"))
        self.assertEqual(54, calculate("(multiply (multiply 2 3) (add 4 5))"))
        self.assertEqual(120, calculate("(multiply (multiply 2 3) (multiply 4 5))"))

    def test_calculator_three_elements(self):
        self.assertEqual(36, calculate("(add 12 12 12)"))
        self.assertEqual(49, calculate("(add 12 12 12 13)"))
        self.assertEqual(24, calculate("(multiply 2 2 2 3)"))
        self.assertEqual(45, calculate("(multiply (add 2 3) 3 3)"))
        self.assertEqual(75, calculate("(multiply (add 2 3) (add 2 3) 3)"))
        self.assertEqual(125, calculate("(multiply (add 2 3) (add 2 3) (add 2 3))"))
        self.assertEqual(625, calculate("(multiply (add 2 3) (add 2 3) (add 2 3) (add 2 3))"))
        self.assertEqual(28, calculate("(add (multiply 2 3) (multiply 4 5) (multiply 1 2))"))
