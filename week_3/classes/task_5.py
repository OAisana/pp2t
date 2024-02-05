class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def checkBal(self):
        print(f"Balance : {self.balance}")
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited : {amount}")
    def withdraw(self, money):
        if money > self.balance:
            print("Error! Not enough money")
        else:
            print(f"Withdawn : {money}") 

acc = Account("Aisana")
acc.checkBal()
acc.deposit(500)
acc.checkBal()
acc.withdraw(200)
acc.checkBal()