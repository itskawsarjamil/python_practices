s = "Programming Hero is the best"
t=s.split(' ')
print(len(t))
final_str=''

for word in t:
    i=len(word)
    # print(i,word[i-1])
    
    while i>=1:
        final_str+=word[i-1]
        i=i-1
    final_str+=" "
print(final_str)