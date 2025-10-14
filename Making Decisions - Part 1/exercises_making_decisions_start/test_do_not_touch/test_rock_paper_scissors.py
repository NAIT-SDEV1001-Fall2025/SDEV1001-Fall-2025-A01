import unittest
from io import StringIO
import sys
from unittest.mock import patch

class LeapYearTestCase(unittest.TestCase):
    @patch('random.randint', return_value=1)
    @patch('builtins.input', return_value="1")
    def test_tie(self , mock_input, mock_random):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('rock_paper_scissors.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "The computer is rock. You are rock. It is a draw"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

    @patch('random.randint', return_value=2)
    @patch('builtins.input', return_value="0")
    def test_win(self , mock_input, mock_random):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('rock_paper_scissors.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "The computer is paper. You are scissor. You win"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

    @patch('random.randint', return_value=2)
    @patch('builtins.input', return_value="1")
    def test_lose(self , mock_input, mock_random):
        # Simulate user input

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        exec(open('rock_paper_scissors.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        EXPECTED = "The computer is paper. You are rock. You lose"

        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)
if __name__ == '__main__':
    unittest.main()