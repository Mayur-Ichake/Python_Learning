# Write a program to create a dictionary in Hindi words with value as their english translation. provide user with an option to look it up

'''translator = {"Namskar":"Hello","Duchaki":"Bike","Dev":"God"}
# print(translator)
# print(translator.get("Dev"))
print("Namskar,Duchaki,Dev")
print("Select any one key")
dic = input()
print(translator[dic])    # this & this "print(translator.get(dic))" are same
print(translator.get(dic))
'''
# 2. Write a program to input eight numbers from the user and display the unique numbers(once)

'''unique1 = int(input("Enter a number:"))
unique2 = int(input("Enter a number:"))
unique3 = int(input("Enter a number:"))
unique4 = int(input("Enter a number:"))
unique5 = int(input("Enter a number:"))
unique6 = int(input("Enter a number:"))
unique7 = int(input("Enter a number:"))
unique8 = int(input("Enter a number:"))

s = {unique1,unique2,unique3,unique4,unique5,unique6,unique7,unique8}
print(s)'''

# 3. can we have a set with 18(int) '18' str as a value in it

"""s = {18,"18"}
print(s)
"""
'''s = set()
s.add(18)
s.add("18")
print(s)
'''

# 4. What will be the length of folloeing set is 

"""s = set()
s.add(18)
s.add(18.0)
s.add("18")
s.add("10")
print(len(s))"""

# 5. what is a type of s

"""s = {}
print(type(s))"""

# 6. Create an empty dictionary. Allow four friends to enter their favorite language as value and use key as their name. Assume that the name are unique
"""s = {}

name1 = input("Enter friends name: ")
lang1 = input("Enter language name: ")
s.update({name1:lang1})

name2 = input("Enter friends name: ")
lang2 = input("Enter language name: ")
s.update({name2:lang2})

name3 = input("Enter friends name: ")
lang3 = input("Enter language name: ")
s.update({name3:lang3})

name4 = input("Enter friends name: ")
lang4 = input("Enter language name: ")
s.update({name4:lang4})

print(s)
"""

# 7. If the name of 2 friends are same; what will be happen to the program in problem 6

"""s = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name:lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
s.update({name:lang})

print(s)"""

# 8. can you change the values inside a list which is contained in set s

# s = {12,3,4,"mayur",[1,2]}
s = {12, 3, 4, "mayur", (1, 2)}  # use a tuple instead of a list
