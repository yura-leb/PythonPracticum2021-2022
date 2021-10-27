from collections import Counter
import re

w = int(input())
l = list()
word = ''
while s := input().lower():
    l += re.split(r"[\W\d]", s)
    
##    for char in s:
##        if char.isalpha():
##            word += char
##        else:
##            if word and len(word) == w:
##                c[word] += 1
##            word = ''
    
c = Counter([elem for elem in l if len(elem) == w])
if c:
    maximum = max(c.values())
    print(*sorted([x for x in c if c[x] == maximum]))
