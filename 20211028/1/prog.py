def fib(m, n):
        i = 0
        a = 1
        b = 1
        while i < m:
                a, b = b, a+b
                i += 1
        while i <= n:
                yield a
                a, b = b, a+b
                i +=1

import sys
exec(sys.stdin.read())
