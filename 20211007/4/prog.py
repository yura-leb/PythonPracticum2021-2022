from math import *

def Calc(s, t, u):
    def a(x):
        return eval(s)

    def b(x):
        return eval(t)

    def c(x, y):
        return eval(u)
    
    return lambda x: c(a(x), b(x))

F = Calc(*eval(input()))
print(F(eval(input())))
