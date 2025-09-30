# write a program to find whether a student has passed or failed if it reqiures a total of 40% and of less 33% to pass in each subject to pass. Assume 3 subjects and take marks as an input from the user 

mark1 = int(input("Enter subject mark:"))
mark2 = int(input("Enter subject mark:"))
mark3 = int(input("Enter subject mark:"))

#total of 40% and of less 33% to pass in each subject

total_percentage = ((mark1 + mark2 + mark3)*100)/300

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are passed in all subjects, Congratulations!\nThanks! SPPU...")

else:
    print("You'r failed, try next year\nThanks! SPPU....")