# Errors and Exceptions

# Syntax Errors
# Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:
# Example:
# while True print('Hello world')


# Exceptions
# Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal.
# Example:
10 * (1/0)
# Output: Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# Example:
4 + spam*3
# Output: Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'spam' is not defined
# Example:
'2' + 2
# Output: Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# Handling Exceptions
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# Example:
try:
    print(x)
except:
    print("An exception occurred")
# Output: An exception occurred
# Example:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
# Output: Variable x is not defined
# Example:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
# Output: Hello


# Throw an exception:
# The raise keyword is used to throw an exception.
# Example:
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
# Output: Traceback (most recent call last):
# File "<stdin>", line 2, in <module>
# Exception: Sorry, no numbers below zero
# Example:
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
# Output: Traceback (most recent call last):
# File "<stdin>", line 2, in <module>
# TypeError: Only integers are allowed

# Assert
# The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
# Example:
x = "hello"
assert x == "goodbye", "x should be 'hello'"
# Output: Traceback (most recent call last):
# File "<stdin>", line 2, in <module>
# AssertionError: x should be 'hello'


# Own Exception Class
# To create your own exception class, you must inherit from the Exception class.
# Example:
class MyError(Exception):
    pass

raise MyError("An error occurred")

# Output: Traceback (most recent call last):
# File "<stdin>", line 4, in <module>
# __main__.MyError: An error occurred

# Example:
class MyError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

num = 10
if num > 5:
    raise MyError("Number should not exceed 5", num)

# Output: Traceback (most recent call last):
# File "<stdin>", line 6, in <module>
# __main__.MyError: ('Number should not exceed 5', 10)