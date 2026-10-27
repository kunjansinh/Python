class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"{self.owner} deposited £{amount:.2f}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"{self.owner} withdrew £{amount:.2f}.")

    def transfer(self, recipient, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.__balance:
            print("Transfer failed: insufficient funds.")
        else:
            self.__balance -= amount
            recipient.__balance += amount
            print(
                f"{self.owner} transferred £{amount:.2f} "
                f"to {recipient.owner}."
            )

    def display_balance(self):
        print(f"{self.owner}'s balance: £{self.__balance:.2f}")


# Create two bank accounts
account1 = BankAccount("Alex", 500)
account2 = BankAccount("Sam", 200)

# Perform transactions
account1.display_balance()
account2.display_balance()

print("\n--- Transactions ---")
account1.deposit(100)
account2.withdraw(50)
account1.transfer(account2, 150)

print("\n--- Final Balances ---")
account1.display_balance()
account2.display_balance()