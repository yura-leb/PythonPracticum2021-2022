import unittest
from unittest.mock import MagicMock, patch
from prog.__main__ import solve


class TestSolver(unittest.TestCase):

    def test_not_zero_1(self):
        self.assertEqual(solve(1, -1), 1.0)

    def test_zero(self):
        self.assertEqual(solve(0, 2), None)

    def test_not_zero_2(self):
        self.assertEqual(solve(1, 1), -1.0)
