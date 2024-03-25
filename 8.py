from datetime import date
from datetime import datetime

def decorator(func):

    def wrapped(*args):
        try:
            func
            return func(*args)
        except Exception as e:
            with open('output.txt', 'a') as f:
                print(type(e).__name__, file=f,end=' ')
                print(datetime.now(), file=f)
    return wrapped

@decorator
def function1(ptr, num):
    ptr += num
    return ptr

@decorator
def function2(num1, num2):
    num1 /= num2
    return num1

ptr = str(input())
num = int(input())
num1 = int(input())
num2 = int(input())


function1(ptr, num)
function2(num1, num2)

