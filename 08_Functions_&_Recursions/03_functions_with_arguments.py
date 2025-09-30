# def hey(name,ending):
#     name = input("Enter your name:")
#     print("Good Day,"+name)
#     print(ending)
# hey("name","Thank you!")    
# hey("name","Thank you!")    
# hey("name","Thanks!")    

def hey(name,ending):
    name = input("Enter your name:")
    print("Good Day,"+name)
    print(ending)
    return "ok"
a = hey("name","Thank you!")    
print(a)
a = hey("name","Thank you!") 
print(a)   
a = hey("name","Thanks!")
print(a)