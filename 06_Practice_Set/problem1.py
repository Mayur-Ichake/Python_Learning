# Write a program to find the greatest of four numbers entered by user 

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
c = int(input("Enter number 3:"))
d = int(input("Enter number 4:"))

if(a>b and a>c and a>d):
    print("Greatest number is a",a)
    op = a
if(b>a and b>c and b>d):
    print("Greatest number is b",b)
    op = b
if(c>b and c>a and c>d):
    print("Greatest number is c",c)
    op = c
if(d>b and d>c and d>a):
    print("Greatest number is d",d)
    op = d

print("Your greatest number is",op)

