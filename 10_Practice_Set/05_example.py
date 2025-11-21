# write a class train which has methods a book ticket, get status (no of seats) and get fare information of train running under indian railways 

import random 

class train():

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        self.fro = fro
        self.to = to
        print(f"Your ticket is book {fro} to {to}")

    def status(self):
        print(f"Train {self.trainNo} is on track...")
    
    def getfare(self):
        print(f"train fare in train no: {self.trainNo} from {self.fro} to {self.to} is {random.randint(222,23224)}")

t = train(2435)
t.book("pune","mumbai")
t.status()
t.getfare()