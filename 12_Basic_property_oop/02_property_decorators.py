class Student():
    school_Name = "DPCOE"

    @classmethod
    def name(cls):
        print(f"School name is {cls.school_Name}")
    
    def show(self):
        print(f"School name also {self.school_Name} ")


e = Student()
e.school_Name = 411014
e.name()
e.show()