class employee():
    company = "tesla"

    def show(self):
        print(f"username is an {self.company} company")

class programmer(employee):
    company = "tata"

    def status(self):
        print(f"you are in {self.company} ")

a = employee
b= programmer

print(a.company, b.company)
a.show(employee)
b.