# List declaration

friends = ['Joseph', 'Glenn', 'Sally']  # List of strings
print(friends)

numbers = [1, 2, 3, 4, 5]  # List of integers
print(numbers)

mixed = [1, 'Joseph', 2, 'Glenn']  # List of mixed data types
print(mixed)

# Accessing elements

print(friends[0])  # Joseph
print(friends[-1])  # last item

print(friends[1])  # Glenn
print(friends[1:3])  # Glenn, Sally

# Nested lists

nested = [1, 2, [3, 4], [5, 6]]
print(nested)
print(nested[2])  # [3, 4]
print(nested[2][0])  # 3

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for col in row:
        print(col)

# List operations

friends.extend(['Jen', 'Trevor'])  # Add multiple elements
print(friends)

friends.append('Jen')  # Add single element
print(friends)

friends.insert(1, 'Ellen')  # Insert element at index
print(friends)

friends.remove('Glenn')  # Remove element
print(friends)

friends.pop(1)  # Remove element at index
print(friends)

friends.sort()  # Sort elements
print(friends)

friends.reverse()  # Reverse elements
print(friends)

friends_copy = friends.copy()  # Copy elements
print(friends_copy)

friends.clear()  # Remove all elements
print(friends)

if 'Jen' in friends_copy:  # Check if element exists
    print('Jen is in the list')

print(len(friends_copy))  # Length of list

list1 = [0] * 5  # Create list with 5 zeros
list2 = [1, 2, 3] * 3  # Create list with 3 repetitions

list3 = list1 + list2  # Concatenate lists

list1[::-1] # Reverse list

list4 = list1[:] # Copy list

b = [x*x for x in range(5)] # List comprehension

c = [x for x in b if x % 2 == 0] # List comprehension with condition

d = b[1:4:2] # ab Index bis Index 4 in 2er Schritten