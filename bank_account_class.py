class BankAccount:
    def __init__(self, account_holder, account_number, account_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.account_balance = account_balance

    def account_info(self):
        print()
        print(" ---Account Information---")
        print(f"Name: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.account_balance} Naira")

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True
