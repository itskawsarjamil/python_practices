def clean_string(text):
    output=''
    for char in text:
        if char not in ':,;-.':
            output+=char
    print(output)
    return output
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)