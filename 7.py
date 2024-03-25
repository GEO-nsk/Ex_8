import json

def to_json(func):

    def wrapped(*args):
        func_ans = func(*args)
        result = json.dumps(func_ans)
        return result
    return wrapped

@to_json
def data(ptr):
    return ptr.split()

@to_json
def function1(ptr1, ptr2):
    ptr1 += ptr2
    return ptr1

ptr = str(input())
ptr1 = str(input())
ptr2 = str(input())

print(data(ptr))
print(function1(ptr1, ptr2))
