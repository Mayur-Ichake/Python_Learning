class company:
    name = "Tcs"
    package = "3LPA"
    sh = "Mayur"

    def getinfo(self):
        print(f"{self.sh} is an this {self.name} company , and their package is around {self.package}")

    def greet():
        print("\nhellooo dosto")


mayur = company
print(f"mayur : {mayur.name} , {mayur.package}")        
company.getinfo(mayur )

mayur.greet()