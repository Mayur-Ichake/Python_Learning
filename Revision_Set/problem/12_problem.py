'''Write a program (in any OOP language: Java, C++, Python, etc.) to create a class called BankAccount with the following:
🔹 Data Members
accountNumber
accountHolderName
balance
🔹 Member Functions
deposit(amount) → add amount to balance
withdraw(amount) → subtract amount if balance is sufficient, otherwise show “Insufficient balance”
display() → show account details
Create an object of the class, deposit 5000, withdraw 2000, and display the final details.'''

class BankAccount():
    accountNumber = "CNBA4008346S"
    accountHolderName = "Mayur Santosh Ichake"
    Balance = 440

    # def __init__(self,Balance):
    #     self.Balance = Balance

    def deposit(self,amount):
        self.amount = amount
        print(f"\naccount N0.: {self.accountNumber}\naccount Holder Name: {self.accountHolderName}\nBalance: {self.Balance}\nAmount of Deposit: {self.amount}\nTotal Amount: {self.Balance + self.amount}")
    
    def withdraw(self,amount_withdraw):
        self.amount_withdraw = amount_withdraw
        print(f"Withdraw amount: {amount_withdraw}\nRemaning Balance:{(self.Balance + self.amount) - self.amount_withdraw}")
    
    def display(self):
        return f"\nDeposit:{self.amount} , withdraw:{self.amount_withdraw}"


op = BankAccount()
op.deposit(1000)
op.withdraw(40)
print(op.display())