tuple1 = (11, [22, 33], 44, 55)

# print(tuple1[0])

x = 0
val=222
for item in tuple1:
    if x == 0:
        if isinstance(item, list):
            x = 1
            item[0]=val
            # print(item[0])
            break
print(tuple1)