# ACIT4420_Assignement1_s354362

Answers to the questions and test cases are in the PDF document

Task 1
This Python function is a optimization of an already created code. This function (find_prime_factors) returns all the prime factors of a interger "n". My function handles the even numbers first and then the odd numbers.


Task 2

This python program demonstrates a simple banking system with a base class (BankAccount) and 2 derivated classes (SavingAccount & CheckingAccount). This system have the basic functions like deposit, and information about the balance. It also have special functionality in the derivated classes (interest & transaction fees)


1. Base Class: `BankAccount`
   - Attributes:
     - `account_holder`: The name of the account holder.
     - `balance`: The current balance, initialized to 0.
   - Methods:
     - `deposit(amount)`: Deposits the specified amount to the account.
     - `withdraw(amount)`: Withdraws the specified amount if sufficient funds are available.
     - `account_info()`: Returns the account holder's name and current balance.

2. Derived Class: `SavingsAccount`
   - Inherits all attributes and methods of `BankAccount`.
   - Additional Attribute:
     - `interest_rate`: A fixed interest rate (default 2%).
   - Additional Method:
     - `apply_interest()`: Applies interest to the current balance.

3. Derived Class: `CheckingAccount`
   - Inherits all attributes and methods of `BankAccount`.
   - Additional Attribute:
     - `transaction_fee`: A fixed fee for each withdrawal (default is $1).
   - Method Override:
     - `withdraw(amount)`: Subtracts both the withdrawal amount and the transaction fee from the balance.


