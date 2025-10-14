import unittest
from io import StringIO
import sys
from unittest.mock import patch 

class ScoresTestCase(unittest.TestCase):
    def test_console_output_with_input(self):
        # Simulate user input
        user_input = "10"

        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Simulate user input and run the file
        with patch('builtins.input', side_effect=[10,20,30]):
            exec(open('scores.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip().split("\n")
        output.sort()
        # for item in output:
        #     print(item)

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__
        
        expected_items = [
            'Test Score 1: 10.0',
            'Test Score 2: 20.0',
            'Test Score 3: 30.0',
            'Average Score: 20.0'
        ]
        expected_items.sort()
        # Assert the output is as expected
        self.assertListEqual(output, expected_items)

if __name__ == '__main__':
    unittest.main()