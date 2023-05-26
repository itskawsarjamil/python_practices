list1 = ['a', 'v', 'c', 'd', 'e', 'f']

i = 0
final_dict = {}
# print(list1[i])
# print(len(list1))
while i < len(list1):
    final_dict[list1[i]] = list1[i+1]
    i += 2
print(final_dict)