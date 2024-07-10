# Task 1: Class for Managing Bank Accounts
# Create a Python class called BankAccount that represents a bank account with the following attributes:
# account_number (private): A unique account number.
# account_holder (public): The name of the account holder.
# balance (protected): The account balance.

# Implement the following methods:
# deposit(amount): Adds the specified amount to the account balance.
# withdraw(amount): Subtracts the specified amount from the account balance. Ensure that the balance does not go below zero.
# get_balance(): Returns the current balance.

# __str__(): Returns a string representation of the account.
# __lt__(other): Custom comparison based on balance (less than).
# __eq__(other): Custom equality comparison based on account number.


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.account_holder = account_holder
        self._balance = balance

    
    def get_account_number(self):
        return self.__account_number
    
    
    def set_account_number(self, new_account_number):
        if len(new_account_number) > 8:
            self.__account_number = new_account_number
        else:
            print("Account number can't be smaller than 8 characters!")

    # @property
    # def account_holder(self):
    #     return self.account_holder

    
    def get_balance(self):
        return self._balance
    
    
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Balance can't be negative!")


    
    def get_account_holder(self):
        return self.account_holder

    
    def set_account_holder(self, new_account_holder):
        if len(new_account_holder) > 0:
            self.account_holder = new_account_holder
        else:
            print("New account holder can't be with ZERO characters name!")
    

    def deposit(self, amount):
        self._balance += float(amount)
    
    def withdraw(self, amount):
        self._balance -= float(amount)

    def get_balance(self):
        return self._balance

    
    def __str__(self):
        return f"Owner: {str(self.get_account_holder())}, Balance: {self.get_balance()}"
    
    def __lt__(self, other):
        return self._balance < other._balance

    def __eq__(self, other):   
        return self.__account_number == other.__account_number


bankAccont = BankAccount("12345678", "Pesho", 3000)

print(bankAccont.get_account_holder())
print(bankAccont.get_account_number())
print(bankAccont.get_balance())

print(bankAccont)
print("---------------")
bankAcconts = [
    BankAccount("135518313", "Tosho", 2000),
    BankAccount("235518313", "Gosho", 3000),
    BankAccount("335518313", "Minka", 4000),
    BankAccount("435518313", "Pinka", 2500),
]

sortedBankAccounts = sorted(bankAcconts)

for account in sortedBankAccounts:
    print(account)


