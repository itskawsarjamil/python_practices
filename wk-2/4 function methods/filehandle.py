# with open('handlefile.txt','a') as fileWrite:
#     fileWrite.write('I love python wish i could say that\n')
    
with open('handlefile.txt','r') as fileRead:
    text=fileRead.read()
    print(text)