import unittest
from problems.problem029 import encode, decode


class TestProblem029(unittest.TestCase):

    def test_encode_return_correct_string(self):
        expected = '4A3B2C1D2A'
        actual = encode('AAAABBBCCDAA')
        self.assertEqual(actual, expected)

    def test_decode_return_correct_string(self):
        expected = 'AAAABBBCCDAA'
        actual = decode('4A3B2C1D2A')
        self.assertEqual(actual, expected)
