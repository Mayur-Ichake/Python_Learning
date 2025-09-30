# Write a program using function to convert celsius to  Fahrenheit
"""
formulas:-
Fahrenheit to Celsius -  °C=(°F-32) x 5/9
Celsius to Fahrenheit -   °F=(°C x 9/5) + 32
"""
def c_to_f(c):
     c = (c * 9/5) + 32
     return c

c = int(input("Enter temperature:"))    
print(f"This {(c)}°C Celsius temperature to Fahrenheit is:{(c_to_f(c))}°F")

