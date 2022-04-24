import unittest
from unittest.mock import MagicMock
import prog


class TestSolver(unittest.TestCase):

    eps = 10 ** -7
    
    def check(self, params, correct):
        prog.SquareIO.inputCoeff = MagicMock(side_effect=params)
        prog.SquareIO.printResult = MagicMock()
        prog.solveSquare()
        res = prog.SquareIO.printResult.call_args.args[0]
        if type(res) is str:
            assert res == correct
        elif type(res) is float:
            assert correct - self.eps <= res <= correct + self.eps
        elif type(res) is tuple and len(res) == 2:
            assert correct[0] - self.eps <= res[0] <= correct[0] + self.eps and correct[1] - self.eps <= res[1] <= correct[1] + self.eps
        else:
            assert False

    def test_greater0(self):
        self.check((1, 0, -1), (1.0, -1.0))

    def test_equal0(self):
        self.check((1, -2, 1), (1.0, 1.0))

    def test_less0(self):
        self.check((1, 0, 1), "No solutions: discriminant < 0")

    def test_linear(self):
        self.check((0, 1, 1), -1.0)

    def test_const(self):
        self.check((0, 0, 1), "No solutions for all x")

    def test_all0(self):
        self.check((0, 0, 0), "All x are solutions")
