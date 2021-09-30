a = list(eval(input()))
for i in range(len(a) - 1):
    for j in range(i, len(a)):
        if a[i]**2%100 > a[j]**2%100:
            a[i], a[j] = a[j], a[i]
print(a)
