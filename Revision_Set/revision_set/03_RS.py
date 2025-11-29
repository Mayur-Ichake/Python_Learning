# 1 Write a python program to display a user entered name followed by good  afternoon using input() function

name = input("Enter your name:")
print(f"Good Afternoon {name}")

# 2 Write a program to fill in letter template given below with name and date
letter ='''Dear <|Name|>,
You are selected!
<|Date|>'''

name = input("Enter your name:")

date = input("Enter the date:")
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))

# print("Hello World")