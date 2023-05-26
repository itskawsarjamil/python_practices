import math
import time

def timer(func):
    def inner(*args, **kargs):
        print("Time start")
        start=time.time()
        func(*args, **kargs)
        print('Time End')
        end=time.time()
        print(f'total time taken: {end-start}')
    return inner

@timer
def get_factorial(n):
    result=math.factorial(n)
    print(f'factorial of {n} is:{result}')

get_factorial(8)