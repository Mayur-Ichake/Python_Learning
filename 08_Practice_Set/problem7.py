# Write a python function to remove a given word form a list and strip it at the time

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["mayur","shreya","ma"]        
print(rem(l, "ma"))