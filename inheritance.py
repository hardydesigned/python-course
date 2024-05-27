#Vererbung

class Person:
    def __init__(self, name, age): #Konstruktor
        self.name = name
        self.age = age

    # Self ist ein Verweis auf die Instanz der Klasse
    def myfunc(self):
        print("Hello my name is " + self.name)

#Unterklasse von Person, Anweisung super() ruft den Konstruktor der Elternklasse auf
class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.graduationyear)

x = Student("Mike", 22, 2020)

x.welcome()
