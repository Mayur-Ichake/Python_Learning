# Create an empty dictionary. allow 4 friends to enter their favorite language as value and key as their names. Assume that the names are unique 
d ={}

name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name:lang})
name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name:lang})
name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name:lang})
name = input("Enter friends name:")
lang = input("Enter Language name:")
d.update({name:lang})
print(d)