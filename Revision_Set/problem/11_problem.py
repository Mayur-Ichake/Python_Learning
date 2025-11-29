'''Create a class Book with:
Attributes: title, author, price
Method: get_info() that returns all book details as a formatted string.'''

class book():
    def __init__(self,title,author,price):
        self.title = title 
        self.author = author 
        self.price = price 

    def get_info(self):
        return f"title: {self.title}, Author: {self.author}, price: {self.price}"

op = book("Raja","karn",0.0)
print(op.get_info())  