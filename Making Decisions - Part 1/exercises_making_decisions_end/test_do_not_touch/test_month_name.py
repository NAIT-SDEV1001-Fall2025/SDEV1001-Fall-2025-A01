import unittest
from io import StringIO
import sys
from unittest.mock import patch

class MonthNameTestCase(unittest.TestCase):
    @patch('builtins.input', return_value="4")
    def test_tie(self , mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('month_name.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip().split("\n")[-1]

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "April"

        # Assert the output is as expected
        self.assertEqual(output.lower(), EXPECTED.lower())

   
if __name__ == '__main__':
    unittest.main()