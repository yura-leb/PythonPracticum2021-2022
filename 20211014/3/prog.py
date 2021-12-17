from fractions import Fraction

def scale(length, maximum, x):
    return Fraction(x) * Fraction(length) / Fraction(maximum)

first = input()
w = len(first)
strings = []
while (s := input()) != first:
    strings.append(s[1:-1])

h = len(strings) + 2

gas = 0
liquid = 0
for s in strings:
    if s[0] == '.':
        gas += w - 2
    else:
        break
volume = w * h - 2 * w - 2 * h + 4
liquid = volume - gas
s1 = f'{"."*round(scale(20, max(gas, liquid), gas)):<20} {gas}/{volume}'
s2 = f'{"~"*round(scale(20, max(gas, liquid), liquid)):<20} {liquid}/{volume}'
result = ['#' * h]

if r := liquid % (h-2):
    liquid += h - 2 - r
    gas -= h - 2 - r

gas_rest = gas
liquid_rest = liquid

while gas_rest:
    result.append('#' + (h-2) * '.' + '#')
    gas_rest -= h-2

while liquid_rest:
    result.append('#' + (h-2) * '~' + '#')
    liquid_rest -= h-2

result.append('#' * h)

for s in result:
    print(s)

print(s1)
print(s2)
