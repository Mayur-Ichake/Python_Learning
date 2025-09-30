# A spam comment is defined as a text containsing following keywords 
# "make a lot of money","buy now","subscribe this","click this",write program to detect these spams

text1 = "make a lot of money"
text2 = "buy now"
text3 = "subscribe this"
text4 = "click this" 

msg = input("Enter your msg:")

if((text1 in msg) or (text2 in msg) or (text3 in msg) or (text4 in msg)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")    