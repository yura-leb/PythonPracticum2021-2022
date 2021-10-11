from math import *

def Calc(s, t, u):
    def a(x):
        return eval(s)

    def b(x):
        return eval(t)

    def c(x, y):
        return eval(u)
    
    return lambda x: c(a(x), b(x))

s, t, u = eval(input())
f = Calc(s,t,u)
print(f(eval(input())))
