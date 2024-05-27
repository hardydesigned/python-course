# Lambda functions are small anonymous functions that can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression
# Example:
x = lambda a : a + 10
print(x(5)) # Output: 15

x = lambda a, b : a * b
print(x(5, 6)) # Output: 30

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # Output: 13

# Lambda functions can be used inside functions.
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11)) # Output: 22

mytripler = myfunc(3)

print(mytripler(11)) # Output: 33

# map() function: The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# Syntax: map(function, iterables)
# Example:
def myfunc(n):
    return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(list(x)) # Output: [5, 6, 6]

# The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
# Syntax: filter(function, iterable)
# Example:
def myfunc(x):
    if x < 18:
        return False
    else:
        return True
    
adults = filter(myfunc, [5, 12, 17, 18, 24, 32])
print(list(adults)) # Output: [18, 24, 32]

# The reduce() function is defined in the functools module. Like the map() and filter() functions, the reduce() function receives two arguments, a function and an iterable.
# However, it does not return another iterable, instead it returns a single value.
# Syntax: reduce(function, iterable)
# Example:
from functools import reduce

def myfunc(a, b):
    return a + b

x = reduce(myfunc, [1, 2, 3, 4])

print(x) # Output: 10

# To generate a new list that calculates the square of each number in the list, you can use the map() function.
# Example:
my_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, my_list))

print(squared_list) # Output: [1, 4, 9, 16, 25]

# or do it with loop inside the list

squared_list = [x**2 for x in my_list]