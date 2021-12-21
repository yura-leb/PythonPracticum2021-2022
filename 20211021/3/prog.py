from collections import defaultdict
import re

w = int(input())
l = list()
word = ''
c = defaultdict(int)
while True:
    s = input() + ' '
    if s.split() == []:
        break
    
    s = s.lower()
    for char in s:
        if char.isalpha():
            word += char
        else:
            if word and len(word) == w:
                c[word] += 1
            word = ''
if c:
    maximum = max(c.values())
    print(*sorted([x for x in c if c[x] == maximum]))
