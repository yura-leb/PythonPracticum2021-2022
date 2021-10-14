from math import sin
from fractions import Fraction

##x = [-4,4]
##length = x[1] - x[0]
##part = Fraction(length) / Fraction('80')
##start = x[0]
##pos = start
##while pos <= x[1]:

def scale(A, B, a, b, x):
    return (x - A)/(B - A) * (b - a) + a

f = sin
W, H = 66, 20
A, B = -14, 14
X = [f(scale(0, H+1, A, B, i)) for i in range(H+1)]
Y = [f(x) for x in X]
my, My = min(Y), max(Y)
for y in Y:
    print(int(scale(my, My, 0, W, y))*' ' + '*')
