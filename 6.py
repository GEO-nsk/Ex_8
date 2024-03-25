import json

def decorator(func):

    def wrapped(arg):
        print(func(arg))
        return func(arg)
    return wrapped

@decorator
def string1(ptr):
    ptr += '000'
    return ptr

ptr = str(input())

string1(ptr)

