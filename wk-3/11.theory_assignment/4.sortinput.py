s = 'x3b4U5i2'
# print(s)
final_str = ''
for i, char in enumerate(s):
    # print(char.isalpha(), i, s[i])
    if char.isalpha() and s[i+1].isalpha():
        final_str+=char
        
    elif char.isalpha() and s[i+1].isdigit():
        # print(char*int(s[i+1]))
        final_str+=char*int(s[i+1])

final="".join(sorted(final_str, key=lambda x: ord(x.lower())-ord('a')))
print(final)

