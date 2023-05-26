sample_dict = {'a': 100, 'b': 200, 'c': 300}
val = 100
i = 0
for key, value in sample_dict.items():
    if val == value:
        print("Present")
        i = 1
        break
if i == 0:
    print("Not present")
