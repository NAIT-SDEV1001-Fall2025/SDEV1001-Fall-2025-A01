import unittest
from io import StringIO
import sys
from unittest.mock import patch

class LeapYearTestCase(unittest.TestCase):
    @patch('builtins.input', return_value="2008")
    def test_correct(self , mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('leap_year.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "Is 2008 a leap year? true"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

    @patch('builtins.input', return_value="1900")
    def test_error(self , mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('leap_year.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "Is 1900 a leap year? false"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()