def replace_comma_with_space(text):
    output=""
    for char in text:
        if char ==',':
            output+=' '
        else:
            output+=char
    # print(output)
    return output
    
s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
