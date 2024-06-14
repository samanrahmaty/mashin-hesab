import unittest
from calculator import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = divide(10, 5)
        self.assertEqual(result, 2.0)

    def test_divide_by_zero(self):
        result = divide(10, 0)
        self.assertEqual(result, "Error! Division by zero.")

if name == 'main':
    unittest.main()