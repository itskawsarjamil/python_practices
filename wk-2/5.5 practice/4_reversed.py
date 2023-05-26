list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
print(list(zip(list1,reversed(list2))))
for x,y in zip(list1,reversed(list2)):
    print(x,y)