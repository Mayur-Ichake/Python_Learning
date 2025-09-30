#  Write a python function which converts inches to cm

""" 1 inches = 2.54cm """
def in_to_cm(c):
    if(c == 0):
        return
    return c*2.54

c = int(input("Enter inches:"))
print(f"{(c)} inches is equal to: {(in_to_cm(c))} cm")    