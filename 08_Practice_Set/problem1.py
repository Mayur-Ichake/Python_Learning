# Write a program using function to find greatest of three numbers

def greatest(a,b,c):
      if(a>b and a>c):
            return a
      elif(b>a and b>c):
            return b
      elif(c>a and c>b):
            return c         


a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))

print(f"In this {(a,b,c)} greatest of three numbers is:{(greatest(a,b,c))}")