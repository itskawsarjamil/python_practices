n=8
x = n
y = x
st=''
while x:
    y = x
    z = x
    st=''
    while z:
        if y == z or z == 1:
            st=st+'* '
            # print('*')
            z = z-1
            if z == 0:
                
                print(f'{st}\n')
        else:
            st=st+'  '
            # print(' ')
            z = z-1
    x = x-1
x = 2
y = x
st=''
while x<=n:
    y = x
    z = x
    st=''
    while z:
        if y == z or z == 1:
            st=st+'* '
            z = z-1
            if z == 0:
                
                print(f'{st}\n')
        else:
            st=st+'  '
            z = z-1
    x = x+1