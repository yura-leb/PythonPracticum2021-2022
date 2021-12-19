def Pareto(*args):
    result = []
    if len(args) == 0:
        return ()
    elif len(args) == 2:
        if type(args[0]) == int:
            return (args,)
    for i in range(len(args)):
        for j in range(len(args)):
            if i != j:
                if args[i][0] <= args[j][0] and args[i][1] <= args[j][1] and \
                                 (args[i][0] < args[j][0] or args[i][1] < args[j][1]):
                    break
        else:
            result += (args[i],)
    return tuple(result)

print(Pareto(*eval(input())))

