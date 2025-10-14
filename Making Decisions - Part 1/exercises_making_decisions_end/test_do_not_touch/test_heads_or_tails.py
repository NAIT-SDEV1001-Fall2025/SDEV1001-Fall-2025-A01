import unittest
from io import StringIO
import sys
from unittest.mock import patch

class HeadsOrTailsTestCase(unittest.TestCase):
    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value="h")
    def test_error(self , mock_input, mock_random):
        # Simulate user input
        # user_input = "1"

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('heads_or_tails.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "The coin flip was: tails\nyou guessed wrong!"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

    @patch('random.randint', return_value=0)
    @patch('builtins.input', return_value="h")
    def test_correct(self , mock_input, mock_random):
        # Simulate user input
        # user_input = "1"

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('heads_or_tails.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "The coin flip was: heads\nyou guessed correct!"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()