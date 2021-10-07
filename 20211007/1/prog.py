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



        
print(Pareto((32, 38), (10, 14), (19, 44), (31, 31), (17, 33), (53, 6), (48, 9), (6, 38), (30, 49), (52, 30), (7, 30), (45, 45), (21, 51), (7, 49), (11, 23)))
