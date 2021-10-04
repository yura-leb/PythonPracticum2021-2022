a, b = eval(input())
print([i for i in range(a,b) if all([i%j for j in range(2, i//2+1)])])
