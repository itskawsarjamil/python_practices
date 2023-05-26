a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."


def create_new_string(s):
    output = list()
    t = ""
    for word in s:
        # print(word)
        if word not in ",.":
            t += word
    t = t.lower()
    t = t.split()
    # print(enumerate(t))
    for word in a:
        word = word.lower()
        for j, seword in enumerate(t):
            if j == 0:
                continue

            elif word == t[j-1]:
                output.append(seword)
                continue

    output = " ".join(output)

    with open('handleString.txt', 'a') as fileWrite:
        fileWrite.write(output)

    return output


final_output = create_new_string(s)

print(final_output)
