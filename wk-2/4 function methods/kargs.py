# def long_name(**kargs):
#     print(kargs)


# long_name(first='Dr.', last='Chowdhury', middle='Rahman')


def display(**kwargs):
    for i in kwargs:
        print(i, end=" ")

display(first='Dr.', last='Chowdhury', middle='Rahman')
    