# write a class "Calculator" capable of finding square, cube and sum of number


class calculator():

    def __init__(self,num):

        self.num = num

    def square(self):
        print(f"{self.num} * {self.num} = {self.num*self.num}")

    def cube(self):
        print(f"{self.num} * {self.num} = {self.num*self.num*self.num}")

    def sum(self):
        print(f"{self.num} + {self.num} = {self.num + self.num}")

    def greet():
        print("Welcome to calci....\n")

calculator.greet()
calc = calculator(4)
calculator.square(calc)
calc = calculator(2)
calculator.cube(calc)
calc = calculator(2)
calculator.sum(calc)
