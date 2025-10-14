import unittest
from io import StringIO
import sys
from unittest.mock import patch

class PackageSelectorTestCase(unittest.TestCase):
    @patch('builtins.input', return_value="D")
    def test_working(self , mock_input):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('package_selector.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "You have selected Package D"

        # Assert the output is as expected
        self.assertIn( EXPECTED.lower(), output.lower())

   
if __name__ == '__main__':
    unittest.main()