result = 0
a = 0
a = int(input())
while a > 0:
    result += a
    if result > 21:
        print(result)
        break
    a = int(input())
else:
    print(a)
