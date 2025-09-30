# write a program to find the sum to first n natural numbers using while loop

n = int(input("Enter a number:"))

i = 1
sum = 0
while(i<=n):
    sum+=i
    i+=1
print(sum)    


#  using for loop

i = 1
sum = 0
for i in range(1,n+1):  
    sum +=i
    i +=1
print(sum)    
    

