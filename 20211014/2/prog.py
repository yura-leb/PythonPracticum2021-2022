from math import *

def scale(A, B, a, b, x):
    return (x - A)/(B - A) * (b - a) + a

W, H, A, B, s = input().split()
W, H, A, B = int(W), int(H), int(A), int(B)
f = lambda x: eval(s)
X = [scale(0, W, A, B, i) for i in range(W)]
Y = [f(x) for x in X]
my, My = min(Y), max(Y)
res_Y = [int(scale(my, My, 0, H, f(x))) for x in X]
strings = ['' for _ in range(H)]
for i in range(W):
    for j in range(H):
        if H - j - 1 == res_Y[i]:
            strings[j] += '*'
        else:
            strings[j] += ' '
for string in strings:
    print(string)
