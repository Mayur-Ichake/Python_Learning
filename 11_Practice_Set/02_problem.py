#  Create a class "pets" from a class "animal" and further create a class "Dog" from "pets".
# Add a method "Bark" to class "Dog"

class animal():
        print("There are some pets animal & wild animal:")

class pets(animal):
        print("pets animal are like dog,cat,etc.")

class dog(pets):
    @staticmethod
    def bark():
        print("Dogs voice are: bow bow")


c = dog()
c.bark()