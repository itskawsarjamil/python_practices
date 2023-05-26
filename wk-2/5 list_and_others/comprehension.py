numbers = [12, 34, 65, 67, 89, 33]

odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)
print(odd_numbers)

# comprehension
odd_andfive_dvd_numbers2 = [
    num for num in numbers if num % 2 == 1 if num % 5 == 0]

print(odd_andfive_dvd_numbers2)

names = ['sakib', 'sabbir', 'salman']
ages = [37, 32, 21]
pairs = [(name, age) for name in names for age in ages if age < 25]
print('pairs:', pairs)

for name in names:
    for age in ages:
        if age < 25:
            print(name, age)
