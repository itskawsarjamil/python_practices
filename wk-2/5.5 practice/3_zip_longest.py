from itertools import zip_longest

list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

print(list(l+m for l, m in zip_longest(list1, list2,fillvalue=0)))
