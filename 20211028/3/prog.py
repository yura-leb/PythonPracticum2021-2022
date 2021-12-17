import itertools

print(', '.join(sorted(filter(lambda x: x.count('TOR') == 2, map(''.join, itertools.product('TOR', repeat=int(input())))))))
