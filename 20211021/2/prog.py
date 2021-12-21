import math

functions = {}
k = 0
while (s := input().split())[0] != 'quit':
    k+=1
    if s[0][0] == ':':
        fun_name = s[0][1:]
        fun = s[-1]
        functions[fun_name] = (fun, s[1:-1])
    elif s[0] in functions:
        args = functions[s[0]][1]
        d = dict(zip(args, map(eval, s[1:])))
        print(eval(functions[s[0]][0], math.__dict__, d))
    else:
        print("Wrong str")

print(eval(s[1]).format(len(functions) + 1, k+1))

