a = int(input())
if not a % 2 and not a % 25:
    print('A +', end=' ')
else:
    print('A -', end=' ')

if a % 2 and not a % 25:
    print('B +', end=' ')
else:
    print('B -', end=' ')
    
if not a % 8:
    print('C +')
else:
    print('C -')
