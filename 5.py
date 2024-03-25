from functools import reduce

a = int(input())
b = int(input())
c = int(input())

doc = []

for itr in range(a, b+1):
    if itr ** 0.5 % c == 0:
        doc.append(itr)

print(reduce(lambda x, y: x * y, doc))