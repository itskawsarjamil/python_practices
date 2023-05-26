sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
# print(keys[1])


new_dict={key:value for key,value in sample_dict.items() for val in keys if key==val}

print(new_dict)
