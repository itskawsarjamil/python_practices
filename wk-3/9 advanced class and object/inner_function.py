def do_something():
    print("Inside the function do_something")
    def inner_function():
        print('Inside the inner function')
    inner_function()
    
def first_function():
    print('Inside the first function')
    def second_function():
        print('inside the inner function')
    return second_function

# do_something()

first_function()()