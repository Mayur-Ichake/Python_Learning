class Animal:
    @staticmethod
    def animals():
        print("Above animals and there voice....")

    def animal_1(self,name,voice):
        print(f"{name}")
        print(f"{name} voice is {voice}")


    def greet(self,your_name):
        print(f"Thank you {your_name} to visit our pet app.....")


km = Animal()
km.animals()
km.animal_1("Dog","Barks")
km.greet("Mayur")
