class Employee():
    name = input("Enter Your Name: ")
    salary = int(input("Enyter Your Current Salar: "))
    joined_month = input("Enter Your Joined Month: ")

Employee()
print(f"\nName: {Employee.name}\nMonth: {Employee.joined_month}")
