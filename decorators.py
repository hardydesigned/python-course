# There are function and class decorators in Python.

# Function Decorators
# A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()

# The above code is equivalent to:
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# With parameters

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(add5(10))

# Decorators with repeated code

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("World")

# Class Decorators

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)
    
@CountCalls
def say_hello():
    print("Hello!")

say_hello()

# Decorators are used in web frameworks like Flask and Django to create routes.
# Decorators are used in testing frameworks like pytest to mark functions as tests.
# Decorators are used in logging to log the time of execution of functions.
# Decorators are used in authorization and authentication.
# Decorators are used in debugging to print the arguments a function is called with.
# Decorators are used in memoization to cache the return values of functions.
#  Decorators are used in data validation to check if the correct data type is passed to a function.
# Decorators are used in timing functions to calculate the time a function takes to execute.
# Decorators are used in database connections to open and close connections.
# Decorators are used in API rate limiting to limit the number of requests that can be made to an API.
# Decorators are used in caching to cache the return values of functions.
# Decorators are used in error handling to catch exceptions.
# Decorators are used in class methods and static methods.
# Decorators are used in property getters and setters.
