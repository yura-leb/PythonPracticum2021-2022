import sys

s = sys.stdin.buffer.read()
N = s[0]
L = len(s) - 1
lines = []
for i in range(N):
    lines.append(s[1 + int(i * L / N) : 1 + int((i+1) * L / N)])

sorted_lines = sorted(lines)
res = s[0:1] + b''.join(sorted_lines)
sys.stdout.buffer.write(res)
