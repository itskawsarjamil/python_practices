
def all_types(first, *args, **kargs):#parameter name can be different
    print("first",first)
    for word in args:
        print(word)
    print(kargs)
    for key, value in kargs.items():
        print(key, value)




all_types('abd', 'ddd', 'kjk', 'lll', 'pp', name='Abul', father='babul')



