class BankAccount:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Not enough money')

    def account_info(self):
        return f"Account holder: {self.account_holder}, Balance: {self.balance:.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder)
        self.balance = balance 
        self.interest_rate = 0.02
    
    def apply_interest(self):
        self.balance = self.balance*(1+self.interest_rate)
    
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder)
        self.balance = balance
        self.transaction_fee = 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance-amount-self.transaction_fee
        else: print('You do not have enough money')

x = CheckingAccount("Naveen",1000)
x.deposit(10)
x.withdraw(500)
print(x.account_info())