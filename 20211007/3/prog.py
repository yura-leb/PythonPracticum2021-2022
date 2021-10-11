def Bisect(elem, line):
    if not line or sorted(line) != list(line):
        return False
    if len(line) == 1:
        if elem != line[0]:
            return False
        else:
            return True
    else:
        middle = len(line) // 2
        if elem == line[middle]:
            return True
        elif elem < line[middle]:
            return Bisect(elem, line[0:middle])
        else:
            return Bisect(elem, line[middle+1:len(line)])

elem, line = eval(input())
print(Bisect(elem, line))


