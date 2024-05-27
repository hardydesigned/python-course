#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is unordered, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values.
#Keys are used to access values.
#Keys must be unique.
#Values can be of any data type.
#Dictionaries are mutable, meaning they can be changed after they are created.
#Dictionaries are optimized for retrieving data.
#Dictionaries are similar to JSON objects.

monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

print(monthConversions['Nov'])  # November
print(monthConversions.get('Dec'))  # December
print(monthConversions.get('Luv', 'Not a valid key'))  # Not a valid key

#Dictionary operations

print(monthConversions.keys())  # Get keys
print(monthConversions.values())  # Get values
print(monthConversions.items())  # Get key-value pairs

monthConversions['Luv'] = 'Love'  # Add key-value pair
print(monthConversions)

monthConversions.pop('Luv')  # Remove key-value pair
print(monthConversions)

monthConversions.popitem()  # Remove last key-value pair
print(monthConversions)

monthConversions.clear()  # Remove all key-value pairs
print(monthConversions)

d = dict(a=1, b=2, c=3)  # Create dictionary without ""

tuple = (1, 2, 3)
dict = {tuple: 'Tuple'}  # Create dictionary with tuple as key