import unittest
from io import StringIO
import sys

class FixMeTestCase(unittest.TestCase):
    def test_console_output(self):
        # Redirect stdout to a StringIO object
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the file
        exec(open('fix_me.py').read())

        # Get the value of the captured output
        output = captured_output.getvalue().strip()

        # Reset stdout to its original value
        sys.stdout = sys.__stdout__

        EXPECTED = 'hi there\nmy name is \nThe computer running this code'
        # Assert the output is as expected
        self.assertEqual(output, EXPECTED)

if __name__ == '__main__':
    unittest.main()