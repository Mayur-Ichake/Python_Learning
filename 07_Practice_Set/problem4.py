#write a program to find whether a given number is prime or not

n = int(input("Enter a number:"))

i = 1
for i in range(2,n):
    if(n%i) == 0:
        print("This number is not prime")
        i +=1
        break
else:
    print("This number is prime")        
