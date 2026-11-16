import unittest
from unittest.mock import patch

from issue_sample import get_number


class GetNumberTests(unittest.TestCase):
    @patch("builtins.input", return_value="12.5")
    def test_returns_numeric_input(self, mocked_input):
        self.assertEqual(get_number("Number: "), 12.5)
        mocked_input.assert_called_once_with("Number: ")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["hello", "12"])
    def test_retries_non_numeric_input(self, mocked_input, mocked_print):
        self.assertEqual(get_number("Number: "), 12.0)
        mocked_print.assert_called_once_with("Please enter a numeric value.")
        self.assertEqual(mocked_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()
