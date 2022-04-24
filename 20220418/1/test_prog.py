import unittest
from unittest.mock import MagicMock, patch
import prog


class TestSolver(unittest.TestCase):

    def test_greater0(self):
        self.assertEqual(prog.solveSquare(1, 0, -1), (1.0, -1.0))

    def test_equal0(self):
        self.assertEqual(prog.solveSquare(1, -2, 1), (1.0, 1.0))

    def test_less0(self):
        self.assertEqual(prog.solveSquare(1, 0, 1), None)
