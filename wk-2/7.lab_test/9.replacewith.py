replace_with = ["chief", "thief", "superintendent",
                "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."


def replace_word(text):

    output = list()
    t = s.split()
    i = 1

    for word in t:
        if word not in replace_with:
            output.append(word)
            
        else:
            output.append(replace_with[i])
            i += 2
    
    output=" ".join(output)

    return output


output = replace_word(s)
print(output)
