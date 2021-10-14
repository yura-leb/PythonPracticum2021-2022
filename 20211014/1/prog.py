from fractions import *
def f(s, w, *args):
    s = Fraction(s)
    w = Fraction(w)
    power = []
    index = []
    up = Fraction('0')
    down = Fraction('0')
    power1 = int(args[0])
    for i in range(power1 + 1):
        index.append(Fraction(args[i]))
    for power in range(power1 + 1):
        up += index[power] * (s ** (power1 - power))
    power2 = int(args[power1])
    for i in range(power2 + 1):
        index.append(Fraction(args[i]))
    for power in range(power2 + 1):
        down += index[power] * (s ** (power2 - power))
    result = up / down
    print(type(result))
    return result == w


