from fractions import *

def f(s, w, args):
    index = []
    up = Fraction('0')
    down = Fraction('0')
    power1 = int(args[0])
    for i in range(1, power1 + 2):
        index.append(Fraction(args[i]))
    for power in range(power1 + 1):
        up += index[power] * (s ** (power1 - power))
    power2 = int(args[power1 + 2])
    index = []
    for i in range(power1 + 3, power1 + power2 + 4):
        index.append(Fraction(args[i]))
    for power in range(power2 + 1):
        down += index[power] * (s ** (power2 - power))
    return up / down == w if down else False

a = input().strip().split(', ')
s = Fraction(a[0])
w = Fraction(a[1])
print(f(s, w, a[2:]))

