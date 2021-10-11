def Pareto(*args):
    result = ()
    for i in range(len(args)):
        for j in range(len(args)):
            if i != j:
                if args[i][0] <= args[j][0] and args[i][1] <= args[j][1] and \
                                 (args[i][0] < args[j][0] or args[i][1] < args[j][1]):
                    break
        else:
            result += (args[i],)
    return result

print(Pareto(*eval(input())))

