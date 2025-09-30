'''a = 5
if(a>10):
    print("a is greather")
else:
    print("a is smaller")    '''

# 1. Write a program to find the greatest of four numbers enterned by the user 
'''
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
d = int(input("Enter a number:"))

if(a>b and a>c and a>d):
    print(f"Value of a is {a}, greater number")
elif(b>c and b>d and b>a):
    print(f"Value of b is {b}, greater number")   
elif(c>d and c>a and c>b):
    print(f"Value of c is {c}, greater number")    
elif(d>a and d>b and d>c):
    print(f"Value of d is {d}, greater number")    '''

# 2. write a program to find out a whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject pass assume 3 subject and take marks as an input from the user

'''sub1 = input("Enter 1st subject:")
mark1 = int(input(f"Enter {sub1} marks:"))

sub2 = input("Enter 2nd subject:")
mark2 = int(input(f"Enter {sub2} marks:"))

sub3 = input("Enter 3rd subject:")
mark3 = int(input(f"Enter {sub3} marks:"))

total_percentage = (mark1+mark2+mark3)/3 


if(total_percentage >=40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("Your are pass in all subject")
else:
    print("You are failed!\n Try next year....")    
'''

