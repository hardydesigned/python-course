#Module kann ich in einem anderen Programm importieren und die Funktionen nutzen
#Module gibt es in Python schon viele, z.B. math, random, os, sys, datetime, time, json, csv, requests, ...
#unter https://docs.python.org/3/library/index.html sind alle aufgelistet
#pip installiert weitere Module als Paketmanager
# pip install numpy usw.

# Importiere die Funktionen aus functions.py
import functions as f

# Importiere die Klasse Person aus classes.py
from classes import Person

print(f.add(1, 2))


p1 = Person("John", 36)