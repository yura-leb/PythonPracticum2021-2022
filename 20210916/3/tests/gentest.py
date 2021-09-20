import random

a = int(input())
numbers = []
for i in range(9):
    numbers.append(random.randint(1, 100))
numbers.insert(random.randint(0, 9), a)
print(numbers)
