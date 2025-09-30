# 1. write a program to store seven fruits in a list entered by the user
'''
fruits = []
fruits_name = input("Enter a fruit name:")
# print(fruits.append(fruits_name))     this is wrong syntax "None"
fruits.append(fruits_name)
fruits_name_2 = input("Enter a fruit name:")
fruits.append(fruits_name_2)
fruits_name_3 = input("Enter a fruit name:")
fruits.append(fruits_name_3)
fruits_name_4 = input("Enter a fruit name:")
fruits.append(fruits_name_4)
fruits_name_5 = input("Enter a fruit name:")
fruits.append(fruits_name_5)
fruits_name_6 = input("Enter a fruit name:")
fruits.append(fruits_name_6)
fruits_name_7 = input("Enter a fruit name:")
fruits.append(fruits_name_7)
print(fruits)

'''
# 2. write a program to accept mark of 6 student in sorted manner

'''Students_marks = [99,78,83,45,35,65]
Students_marks.sort()
print("The marks of 6 students in sorted manner is:",Students_marks)
print(Students_marks)
'''

# 3. Check that tuple type cannot change in python
'''
tuple = (34,"mayur",34.34)
tuple[0] = 10
print(tuple)'''

# 4. Write a program to sum a list with 4 numbers

'''list = [10, 5, 5, 70, 10]
print(sum(list))
'''

# 5. Write a program to count a number of zero in the following tuple

zero = (1,2,3,0,5,6,0,7,8,9,0,10)
print(zero.count(0))  
