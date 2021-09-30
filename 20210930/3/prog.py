a = eval(input())
matrix_1 = []
matrix_1.append(a)
n = len(a)
for i in range(1, n):
    matrix_1.append(eval(input()))

matrix_2 = []
result = [[0 for i in range(n)] for i in range(n)] 
for i in range(n):
    matrix_2.append(eval(input()))
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix_1[i][k] * matrix_2[k][j]
for i in range(n):
    print(result[i])
