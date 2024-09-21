class BankAccount:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print(f'A deposit of {amount:.2f}$ has been done. New total in the account: {self.balance:.2f}$')
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount:.2f}$ has been withdrawn. New total in account: {self.balance}$')
        else:
            print(f'You do not have enough money in the bank to withdraw {amount:.2f}$')

    def account_info(self):
        return f"Account holder: {self.account_holder}, Balance: {self.balance:.2f}$ \n"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder) 
        self.interest_rate = 0.02
    
    def apply_interest(self):
        self.balance = self.balance*(1+self.interest_rate)
        print(f'An interest of {self.interest_rate*100}% has been added. New total: {self.balance:.2f}$')
    
class CheckingAccount(BankAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.transaction_fee = 1

    def withdraw(self, amount):
        tot_amount = amount + self.transaction_fee
        if amount <= self.balance:
            self.balance = self.balance-tot_amount
            print(f'{amount:.2f}$ has been withdrawn from your account. Plus a transaction fee of {self.transaction_fee:.2f}$ dollar has been added. New Total: {self.balance:.2f}$')
        else: 
            print(f'You do not have enough money in the bank to withdraw {tot_amount:.2f}$')

# Testing BankAccount
print('\n---Testing BankAccount---')
x = BankAccount("Naveen")
x.deposit(10000)
x.withdraw(500)
x.withdraw(10000)
print(x.account_info())

# Testing SavingsAccount
print('---Testing SavingsAccount---')
x = SavingsAccount("Naveen")
x.deposit(10000)
x.apply_interest()
print(x.account_info())

# Testing CheckingAccount
print('---Testing CheckingAccount---')
x = CheckingAccount("Naveen")
x.deposit(10000)
x.withdraw(500)
x.withdraw(10000)
print(x.account_info())