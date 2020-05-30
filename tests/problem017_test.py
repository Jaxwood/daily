import unittest
from problems.problem017 import parse, longest_path


class TestProblem017(unittest.TestCase):

    def test_stream(self):
        s = parse("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
        self.assertEqual(longest_path(s), 32)
