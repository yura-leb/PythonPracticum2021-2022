import curses


def solveSquare(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        return ((-b + discriminant**0.5) / (2 * a), (-b - discriminant**0.5) / (2 * a))
    else:
        return None


if __name__ == "__main__":
    import sys
    res = adder(sys.argv[1], sys.argv[2])
