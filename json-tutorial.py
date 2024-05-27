# JSON in Python
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write. It is easy for machines to parse and generate. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.
# Python has a built-in package called json, which can be used to work with JSON data.
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# Serialize JSON - Convert from Python to JSON

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
person_json = json.dumps(person, indent=4, sort_keys=True) # indent=4 -> pretty print
print(person_json)

# Deserialize JSON - Convert from JSON to Python
person = json.loads(person_json)
print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'hasChildren': False, 'titles': ['engineer', 'programmer']}

# With classes
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

user_json = json.dumps(user.__dict__)
print(user_json) # Output: {"name": "Max", "age": 27}

user = json.loads(user_json)
print(user) # Output: {'name': 'Max', 'age': 27}
