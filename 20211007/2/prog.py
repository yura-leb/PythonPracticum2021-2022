def SUB(a, b):
    result = []
    if '__sub__' in dir(a):
        return a - b
    else:
        for elem in a:
            for second in b:
                if elem == second:
                    break
            else:
                result.append(elem)
    return type(a)(result)

a, b = eval(input())
print(SUB(a,b))
