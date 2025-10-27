import unittest
from io import StringIO
import sys
from unittest.mock import patch

class BirthdaysTestCase(unittest.TestCase):

    def test_correct(self):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('pizza_prices.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED_PRICE = "$21.535"
        # Assert the output is as expected
        self.assertIn(EXPECTED_PRICE, output)

if __name__ == '__main__':
    unittest.main()