'''🧪 OOP Practical Question #4 — Encapsulation (Getter & Setter)
Create a class called Student with:
🔹 Private Data Members
__name
__marks
🔹 Functions
setDetails(name, marks) → set values inside private members
getDetails() → display name & marks
calculateGrade() →
Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Otherwise → Grade D
Create an object of class Student, set details for a student, then show the details and grade.'''


class Student:
    def __init__(self):
        self.__name = ""  # private variable

    # Setter
    def setName(self, name):
        self.__name = name

    # Getter
    def getName(self):
        return self.__name


obj = Student()
obj.setName("Mayur")     # setter called
print(obj.getName())     # getter called
