# write a class "Calculator" capable of finding square,cube and square root of number

class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"{self.n} square is {self.n*self.n}")
    def cube(self):
        print(f"{self.n} cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"{self.n} squareroot is {self.n**1/2}")

sq = calculator(2)
sq.square()
sq.cube()
sq.squareroot()