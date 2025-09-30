# Create a class "Programmer" for storing information of few programmers working microsoft

class programmer:
    def __init__(self):
        print("Above info are employees working in microsoft")

    def get_info(self,name, age, place):
        self.name = name
        self.age = age
        self.place = place
        print(f"Employee name: {name}\nAge:{age}\nPlace:{place}")

    @staticmethod
    def greet():
        print("Keep this info is safe hand")   

hello = programmer()
hello.get_info("Mayur",20,"pune")   
hello.get_info("shreya",20,"pune")   
hello.greet()      