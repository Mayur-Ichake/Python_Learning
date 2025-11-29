#  Write a Python program to display calendar

import calendar

year = int(input("Enter a Year: "))
month = int(input("Enter a month: "))

cal = calendar.month(year, month)
print(cal)