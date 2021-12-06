import sys

s = sys.stdin.buffer.read()
start = s[0]
size = (len(s) - 1) // start
if not size:
    size = 1
lines = []
for i in range((len(s) - 1) // size + 1):
    lines.append(s[1 + i * size : 1 + (i+1) * size])

sorted_lines = sorted(lines)
res = s[0:1]
for elem in sorted_lines:
    res += elem
sys.stdout.buffer.write(res)
