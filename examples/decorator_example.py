"""
Ryu uses decorators a lot.
This is a simple example program for me to learn how to use
them. 
Decorators change the behaviour of a function without
modifying the function itself.
"""

#functions are objects
def my_function():
    print('I am a function')

a_function = my_function

a_function()
#output: I am a function

#you can nest functions
def outer_function():
    def inner_function():
        print("Inside the inner function")
    inner_function()

outer_function()
#Output: I came from the inner function
#calling inner_function() returns an error
#it is only available locally inside outer_function
#decorators take the following format
"""
def function_decorator(func):
    def wrapped_func():
        #do something before function
        func()
        #do something after function
    return wrapped_func
"""

#simple example: add borders to a print statement
def add_border(func):
    def wrapped_func():
        print('=' * 30)
        func()
        print('=' * 30)
    return wrapped_func

@add_border
def hello_world():
    print('Hello world!')

hello_world()

#we can also pass arguments using python's *args and **kwargs
def add_border(func):
    def wrapped_func(*args, **kwargs):
        print('=' * 30)
        func(*args, **kwargs)
        print('=' * 30)
    return wrapped_func

@add_border
def greeting(name):
    print("Hello {}!".format(name))

greeting("Alice")
