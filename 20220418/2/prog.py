def solveSquare():
    IO = SquareIO()
    a = IO.inputCoeff("a")
    b = IO.inputCoeff("b")
    c = IO.inputCoeff("c")
    if a:
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            res = ((-b + discriminant**0.5) / (2 * float(a)), (-b - discriminant**0.5) / (2 * float(a)))
        else:
            res = "No solutions: discriminant < 0"
    elif b:
        res = -c / float(b)
    elif c:
        res = "No solutions for all x"
    else:
        res = "All x are solutions"

    IO.printResult(res)


class SquareIO:

    def inputCoeff(self, name):
        return float(input(f"Input {name}: "))

    def printResult(self, result):
        print(f"Solution: {result}")


if __name__ == "__main__":
    solveSquare()