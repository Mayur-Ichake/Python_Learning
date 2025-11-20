class focus:
    name = "Tcs"
    package = "3LPA"

    def __init__(self,company,package,name):
        self.company = company
        self.package = package
        self.name = name


    def getinfo(self):
        print(f"{self.name} is an this {self.company} company , and their package is around {self.package}")

    def greet():
        print("\nhellooo dosto\n")

focus.greet()

mayur = focus("TCS"," 3 LPA" ,"mayur" ) 
focus.getinfo(mayur)
