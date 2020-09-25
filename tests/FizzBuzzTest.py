import io
import unittest
import unittest.mock

from src.solution import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        fizzbuzz(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_match_stdout(self, n, expected_regex, mock_stdout):
        fizzbuzz(n)
        self.assertRegex(mock_stdout.getvalue(), expected_regex)

    def test_only_numbers(self):
        self.assert_stdout(2, '1\n2\n')

    def test_fizz(self):
        self.assert_stdout(4, '1\n2\nFizz\n4\n')

    def test_new_fizz(self):
        self.assert_stdout(14, '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\nFizz\n14\n')

    def test_fizz_buzz(self):
        self.assert_stdout(15, '1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\nFizz\n14\nFizzBuzz\n')

    def test_distant_buzz(self):
        self.assert_match_stdout(53, '\n49\nBuzz\nFizzBuzz\nBuzz\nFizzBuzz\n')
