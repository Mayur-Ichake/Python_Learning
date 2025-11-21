# create a class with a class attribute a; create a object from it and set 'a' directly using object. a=0.Does this change the class attribute

class demo:
    a = 4

op = demo()
print(op.a)
op.a = 0
print(op.a)
print(demo.a)

# no, class attribute will not change

