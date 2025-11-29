'''🧪 OOP Practical Question #2 — Inheritance
Write a program to create a base class called Person with:
🔹 Data Members
name
age
🔹 Member Function
display() → Show person details
Create a derived class called Employee that inherits from Person and adds:
🔹 Data Members
employeeID
salary
🔹 Member Function
show() → Display all details including inherited ones
Create an object of Employee and display the details.'''

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")

class Employee(Person):
    def __init__(self,name,age,employeeID,salary):
        super().__init__(name,age)
        self.EmployeeID = employeeID
        self.salary = salary

    def show(self):
        self.display()
        print(f"EmployeeID: {self.EmployeeID}\nsalary: {self.salary}")

op = Employee("Mayur",21,"JAG76",2343645)
op.show()