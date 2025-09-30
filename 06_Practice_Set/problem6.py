# Write a program to calculate the grade of a student from his marks from the following scheme
"""
90-100 = Ex 
80-90 = A
70-80 = B
60-70 = C
50-60 = D
<50 = f"""

your_marks =int(input("Enter your marks:"))

if(your_marks<=100 and your_marks>=90):
    print("Your grade is Ex:",your_marks)

elif(your_marks<=90 and your_marks>=80):
    print("Your grade is A:",your_marks)

elif(your_marks<=80 and your_marks>=70):
    print("Your grade is B:",your_marks)

elif(your_marks<=70 and your_marks>=60):
    print("Your grade is C:",your_marks)

elif(your_marks<=60 and your_marks>=50):
    print("Your grade is D:",your_marks)

elif(your_marks<=50):
    print("you're fail & your grade is F",your_marks)

else:
    print("Sppu...")    

print("Thanks!")    