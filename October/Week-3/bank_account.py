class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero.")
            return

        self.balance += amount
        print(f"Deposited: £{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawn: £{amount:.2f}")

    def display_balance(self):
        print(f"{self.owner}'s balance: £{self.balance:.2f}")


account = BankAccount("Alex", 100)

account.display_balance()
account.deposit(50)
account.withdraw(30)
account.display_balance()