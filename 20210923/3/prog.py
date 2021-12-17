n = int(input())
a = n
b = n
while a < n + 3:
    while b < n + 3:
        digit_sum = 0
        c = abs(a*b)
        while c != 0:
            digit_sum += c % 10
            c //= 10
        if (digit_sum != 6):
            print(str(a) + '*' + str(b) + '=' + str(a*b), sep='', end=' ')
        else:
            print(str(a) + '*' + str(b) + '=:=)', sep='', end=' ')
        b += 1
    a += 1
    b = n
    print()
