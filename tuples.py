#Tuples declaration
#Tuples werden für Daten verwendet, die nicht verändert werden sollen
#Tuples sind immutable, also man kann nicht hinzufügen, löschen oder ändern
#Tuples sind schneller als Listen

friends = ('Joseph', 'Glenn', 'Sally')  # Tuple of strings
print(friends)

numbers = (1, 2, 3, 4, 5)  # Tuple of integers
print(numbers)

mixed = (1, 'Joseph', 2, 'Glenn')  # Tuple of mixed data types
print(mixed)

#Accessing elements

print(friends[0])  # Joseph
print(friends[1])  # Glenn
print(friends[1:3])  # Glenn, Sally

#Nested tuples

nested = (1, 2, (3, 4), (5, 6))
print(nested)

print(nested[2])  # (3, 4)

print(nested[2][0])  # 3

#Tuple operations

friends_copy = friends  # Copy elements
print(friends_copy)

friends = friends + ('Jen', 'Trevor')  # Add multiple elements
print(friends)

friends = friends + ('Jen',)  # Add single element
print(friends)

friends = friends[:2] + ('Ellen',) + friends[2:]  # Insert element at index
print(friends)

friends = friends[:2] + friends[3:]  # Remove element
