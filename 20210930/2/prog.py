a, b = eval(input())
l = list()
c = [i for i in range(a, b)]
for r in c:
    for t in range(2, r):
        if not r % t:
            break
    else:
        l.append(r)
print(l)

