#  Write a Python program to do arithmetical operations addition and division

#addition 

num1 = float(input("Enter a first number to adding: "))
num2 = float(input("Enter a second number to adding: "))

print(num1 + num2)

#Division

div1 = float(input("Enter a first number to division: "))
div2 = float(input("Enter a second number to division: "))
if (div1 and div2 == 0):
    print("You Enter a zero number please enter correct number")
else:
    print(f"{div1} / {div2} = {div1/div2}")    
    