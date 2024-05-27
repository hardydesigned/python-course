#Strings
#Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

normalString = 'Hello World'
print(normalString)

block = '''Hello
World'''
print(block)

char = normalString[0]

reverse = normalString[::-1]

lis3 = normalString.split(' ')

#Best method to join list of strings, super fast
lis4 = ' '.join(lis3)

lis5 = ['a'] * 10

#String formatting

name = 'John'
age = 25
print('My name is {0} and I am {1} years old'.format(name, age))

#F-strings

print(f'My name is {name} and I am {age + 10} years old')

