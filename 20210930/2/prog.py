a, b = eval(input())
print([i for i in range(max(a, 2),b) if all([i%j for j in range(2, i//2+1)])])
