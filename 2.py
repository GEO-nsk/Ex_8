a = int(input())
b = int(input())
c = int(input())
d = int(input())

def is_multiply(num):
    if num % c == 0 and num % d == 0:
        return True
    else:
        return False

doc = []

for itr in range(a, b+1):
    doc.append(itr)

print(doc)

print(sum(list(filter(is_multiply, doc))))

