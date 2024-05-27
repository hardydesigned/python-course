# Generators
# A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration

# Generators are memory efficient because they only load the data they need to return one value at a time.
# Generators are often used in Python to work with large datasets.

print(sum(my_generator()))

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
print(next(cd))

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(sum(firstn(10)))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10)))

# Typical example is fibonacci sequence

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)


# Generator expressions
# Just like list comprehensions, we can easily create generator expressions.

my_generator = (i for i in range(10) if i % 2 == 0)
mylist = [i for i in range(10) if i % 2 == 0]
for i in my_generator:
    print(i)

print(list(my_generator))
