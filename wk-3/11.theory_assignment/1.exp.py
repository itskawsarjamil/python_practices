numbers=input("enter numbers:")

a,b=numbers.split()

c=1
for i in range(int(b)):
    c=c*int(a)
print("result is:",c)