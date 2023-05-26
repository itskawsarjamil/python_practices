from functools import cache
import time

@cache
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

start =time.time()

for i in range(35):
    print(i,fib(i))

end=time.time()

time_waste=(end-start)
print(time_waste ,'seconds')