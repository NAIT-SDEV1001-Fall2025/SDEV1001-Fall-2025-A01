import unittest
from io import StringIO
import sys
from unittest.mock import patch

class BirthdaysTestCase(unittest.TestCase):

    NAME = "dan"
    NAME_NOT_IN_DICTIONARY = "quince"

    @patch('builtins.input',side_effect=[NAME])
    def test_correct(self, mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('birthdays.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_DATE_IN_OUTPUT = "april 14th"
        # Assert the output is as expected
        self.assertIn(self.NAME, output)
        self.assertIn(EXPECTED_DATE_IN_OUTPUT, output)

    @patch('builtins.input',side_effect=[NAME_NOT_IN_DICTIONARY])
    def test_not_in_dictionary(self, mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('birthdays.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_OUTPUT = "Sorry, we don't have"
        # Assert the output is as expected
        self.assertIn(self.NAME_NOT_IN_DICTIONARY, output)
        self.assertIn(EXPECTED_OUTPUT, output)


if __name__ == '__main__':
    unittest.main()