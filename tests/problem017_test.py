import unittest
from problems.problem017 import longest_path


class TestProblem017(unittest.TestCase):

    def test_stream(self):
        self.assertEqual(longest_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", '\n\t'), 32)