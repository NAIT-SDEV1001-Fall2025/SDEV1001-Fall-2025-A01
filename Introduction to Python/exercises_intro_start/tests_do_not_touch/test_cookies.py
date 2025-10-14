import unittest
from io import StringIO
import sys
from unittest import mock

class CookieTestCase(unittest.TestCase):
    def test_console_output_with_input(self):
        # Simulate user input
        user_input = "25"

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        with mock.patch('builtins.input', return_value=user_input):
            exec(open('cookies.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "You ate 25 cookies\nWhich is equal to: 1875.0 calories"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()