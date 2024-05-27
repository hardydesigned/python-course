#Klassen

class Person:
    def __init__(self, name, age): #Konstruktor
        self.name = name
        self.age = age

    # Self ist ein Verweis auf die Instanz der Klasse
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)