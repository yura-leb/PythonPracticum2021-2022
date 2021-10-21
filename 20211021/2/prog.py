import math

def f(var, fun):
    return lambda var: eval(fun, math.__dict__, var)

functions = {}
while (s := input().split())[0] != 'quit':
    if s[0][0] == ':':
        fun_name = s[0][1:]
        functions[fun_name] = f(eval(s[1]), s[2])
    elif s[0] in functions:
        print(functions[s[0]](eval(s[1])))
    else:
        print("Wrong str")
else:
    print(len(functions) + 1)
