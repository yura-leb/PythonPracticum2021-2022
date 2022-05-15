import unittest
from unittest.mock import MagicMock, patch
from prog import solve


class TestSolver(unittest.TestCase):

    def test_greater0(self):
        self.assertEqual(solve(1, -1), 1.0)

    def test_equal0(self):
        self.assertEqual(solve(0, 2), None)

    def test_less0(self):
        self.assertEqual(solve(1, 1), -1.0)
