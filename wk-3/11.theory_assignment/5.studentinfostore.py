import uuid
info = input("name and mark:")
print(info)
name, mark = info.split()
print(name)
print(mark)

id = uuid.uuid4()

result = f"name: {name} mark: {mark} id: {id}\n"
print(result)
with open('student_info.txt', 'a') as fileWrite:
    fileWrite.write(result)
    fileWrite.close()
