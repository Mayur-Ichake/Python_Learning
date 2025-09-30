class students:
    Branch = "ENTC"
    year = "BE"
    def greet(self):
        print(f"Above all students are {self.Branch} department and they in {self.year} ")

    def getinfo(self,name):
        print(f"{name}, Next week placement drive will come be prepered")    

    @staticmethod
    def suggest():
        print("All the best....")

mayur = students()
mayur.greet()
mayur.getinfo("mayur")
students.suggest()