s = input().lower()
pairs = set()
for i in range(1, len(s)):
    if s[i-1].isalpha() and s[i].isalpha():
        if not s[i-1:i+1] in pairs:
            pairs.add(s[i-1:i+1])
print(len(pairs))
