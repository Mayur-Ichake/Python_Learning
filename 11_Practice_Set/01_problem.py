# Create a class (2-D vector)  and use it to create another class representing a 3-D vector

class twoVector():
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The two Vector is {self.i}i + {self.j}j")        

class threeVector(twoVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show_threeVector(self):
        print(f"The three Vector is {self.i}i + {self.j}j + {self.k}k")

a = twoVector(2,3)
b = threeVector(1,32,5)        

a.show()
b.show_threeVector()