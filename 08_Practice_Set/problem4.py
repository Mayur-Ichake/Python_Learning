# Write a recursion function to calculate the sum of first n natural numbers

"""
sum(3) = 1+(n-1)+n
sum(4) = 1+2+(n-1)+n
sum(5) = 1+2+3+(n-1)+n
sum(n) = 1+2+3+4...+(n-1)+n
sum(n) = sum(n-1)+n
"""
def natural(n):
    if(n == 1 ):
        return 1
    return  natural(n-1)+n
    


n = int(input("Enter a number:"))
print(f"The {(n)} sum of firet n natural number is:{(natural(n))}")