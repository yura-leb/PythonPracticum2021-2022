a = list(eval(input()))
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]**2%100 > a[j+1]**2%100:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
