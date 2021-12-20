class InvalidInput(Exception):
    def __str__(self):
        return 'Invalid input'

class BadTriangle(ZeroDivisionError):
    def __str__(self):
        return 'Not a triangle'

def length(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2)**2) ** (1/2)

def triangleSquare():
    eps = 10 ** (-3)
    while True:
        try:
            (x1, y1), (x2, y2), (x3, y3) = eval(input())
        except Exception:
            print(InvalidInput())
            continue
        try:
            x1, y1, x2, y2, x3, y3 = map(float, (x1, y1, x2, y2, x3, y3))
        except Exception:
            print(BadTriangle())
            continue
        a = length(x1, y1, x2, y2)
        b = length(x1, y1, x3, y3)
        c = length(x2, y2, x3, y3)
        p = (a + b + c) / 2
        square = (p*(p-a)*(p-b)*(p-c)) ** (1/2)
        if -eps < abs(square) < eps:
            print(BadTriangle())
            continue
        else:
            print('%.2f' % square)
            break

triangleSquare()
