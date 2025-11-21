# Create a class "Programmer" for storing information of few programmers working microsoft

class programmer():
    company = "microsoft"

    def __init__(self,name , eligiable_year):
        self.name = name
        self.eligiable_year = eligiable_year

    def greet():
        print("Dear,\n")
    
    
    def getinfo(self):    
        print(f"{self.name} are in this {self.company} company")

programmer.greet()
m = programmer("mayur", 2026)
m.getinfo()
r = programmer("Raju",9900)
r.getinfo()