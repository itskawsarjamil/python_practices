d = {'!': 1, '@': 2, '#': 3, '$': 4, '%': 5, '^': 6}

final_list = list()

def create_list():
    for key, value in d.items():
        print(key, value)
        final_list.extend([key, value])
    print(final_list)
    
create_list()

