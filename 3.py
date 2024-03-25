a = int(input())
b = int(input())
c = int(input())
d = int(input())

doc = []

for itr in range(a, b+1):
    doc.append(itr)

print(sum(list(map(lambda x: x % c != 0 and x % 10 != d, doc))))

