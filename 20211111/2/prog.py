class InvalidInput(Exception):
    pass

class BadTriangle(ZeroDivisionError):
    pass

def length(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2)**2) ** (1/2)

def triangleSquare():
    while True:
        try:
            print(1)
            (x1, y1), (x2, y2), (x3, y3) = eval(input())
            x1, y1, x2, y2, x3, y3 = map(float, (x1, y1, x2, y2, x3, y3))
            
        except Exception:
            print('Invalid Input')
            continue
        a = length(x1, y1, x2, y2)
        b = length(x1, y1, x3, y3)
        c = length(x2, y2, x3, y3)
        p = (a + b + c) / 2
        square = (p*(p-a)*(p-b)*(p-c)) ** (1/2)
        try:
            1/square
        except:
            print('Not a triangle')
            continue
        else:
            break
    return square

##import sys
##exec(sys.stdin.read())
