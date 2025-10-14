import unittest
from io import StringIO
import sys
from unittest import mock

class AcresTestCase(unittest.TestCase):
    def test_console_output_with_input(self):
        # Simulate user input
        user_input = "25"

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        with mock.patch('builtins.input', return_value=user_input):
            exec(open('acres.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip().split("\n")[1]
        print(output)

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "Which is equal to: 1089000 square feet"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()