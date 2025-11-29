'''🧪 OOP Practical Question #3 — Polymorphism (Method Overriding)
Create a base class called Animal with:
🔹 Member Function
sound() → print a generic sound like "Animal makes sound"
Create two derived classes:
1️⃣ Dog → override sound() to print "Dog barks"
2️⃣ Cat → override sound() to print "Cat meows"
Create objects of each class and call the sound() function to demonstrate runtime polymorphism.'''

class Animal():
    def sound(self):
        print("Animals Sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
    

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animal = [Animal(),Dog(),Cat()]

for a in animal:
    a.sound()

