import unittest

from issue_sample import add, calculate, divide, modulo, multiply, power, subtract


class CalculationTests(unittest.TestCase):
    def test_arithmetic_functions(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(modulo(8, 3), 2)

    def test_calculate_dispatches_to_named_operation(self):
        self.assertEqual(calculate("multiply", 4, 5), 20)

    def test_calculate_rejects_unknown_operation(self):
        with self.assertRaisesRegex(ValueError, "Unsupported operation"):
            calculate("unknown", 4, 5)

    def test_divide_rejects_zero_divisor(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
