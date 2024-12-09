class BankAccount:
    # Class variable
    bank_name = "Tech4GirlsBank"

    def __init__(self, account_holder, balance=0):
        # Initialize instance variables
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Add money to account
        self.balance += amount

    def withdraw(self, amount):
        # Deduct money from the account
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    @staticmethod
    def bank_policy():
        # Print a generous policy message
        print("We are committed to providing excellent customer service.")

    @classmethod
    def get_bank_name(cls):
        # Return the bank name
        return cls.bank_name


# Creating an instance
bankaccount_1 = BankAccount("Jennifer", 2000)

# Deposit money
bankaccount_1.deposit(700)

# Withdraw money
bankaccount_1.withdraw(750)

# Display bank policy
BankAccount.bank_policy()

# Display bank name
print("Bank Name:", BankAccount.get_bank_name())
