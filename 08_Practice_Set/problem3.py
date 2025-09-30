# How do you prevent a python print() function to print a new line at the end 

def func(name):
    print("Hello",name,"Sir")
    print("thank you!" , end="\t")
    print("let's go to the work",end="")

func("Mayur")