from collections import Counter
import re

w = int(input())
l = list()
word = ''
while True:
    s = input()
    if s.split() == []:
        break
    
    s = s.lower();
    l += re.split(r"[\W\d]", s)
    
##    for char in s:
##        if char.isalpha():
##            word += char
##        else:
##            if word and len(word) == w:
##                c[word] += 1
##            word = ''
    
c = Counter([elem for elem in l if len(elem) == w])
print(*sorted([x for x in c if c[x] == max(c.values())]))
