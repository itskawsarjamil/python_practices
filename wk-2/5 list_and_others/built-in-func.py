actors = [
    {'name': "Kawsar Jamil", 'age': 23},
    {'name': "Jamil Kawsar", "age": 26}
]
sorted_actor = sorted(actors, key=lambda actor: actor['age'] ,reverse=True)
print(sorted_actor)
