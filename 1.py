ptr = str(input())
i = int(input())
j = int(input())

def is_upper(symbol):
    return symbol.isupper()

ptr = ptr[i-1:j]

print(len(list(filter(is_upper, ptr))))