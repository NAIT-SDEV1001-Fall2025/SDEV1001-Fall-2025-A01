import unittest
from io import StringIO
import sys
from unittest.mock import patch

class ZodiacTestCase(unittest.TestCase):
    @patch('builtins.input', return_value="1900")
    def test_tie(self , mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('zodiac.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "rat"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

   
if __name__ == '__main__':
    unittest.main()