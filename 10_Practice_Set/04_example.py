# add a static method in 2nd example, to greet the user hello 

class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"{self.n} square is {self.n*self.n}")
    def cube(self):
        print(f"{self.n} cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"{self.n} squareroot is {self.n**1/2}")
    @staticmethod
    def greet():
        print("Hello mayur")

sq = calculator(2)
sq.greet()
sq.square()
sq.cube()
sq.squareroot()