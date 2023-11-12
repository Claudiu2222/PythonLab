class Account:
    def __init__(self , owner):
        self.balance = 0
        self.owner = owner
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.balance += amount
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        if amount > self.balance:
            raise ValueError("not enough balance")
        self.balance -= amount
    def check_balance(self):
        return self.balance
    def __str__(self):
        return "Account of "+self.owner+" with balance "+str(self.balance)
    def __repr__(self):
        return "Account of "+self.owner+" with balance "+str(self.balance)

class SavingsAccount(Account):
    def __init__(self,owner, interest_rate):
        if interest_rate < 0:
            raise ValueError("interest_rate cannot be negative")
        super().__init__(owner)
        self.interest_rate = interest_rate
    def compute_interest(self):
        return self.balance * self.interest_rate
    def add_interest(self):
        self.balance += self.compute_interest()

class CheckingAccount(Account):
    def __init__(self,owner, overdraft_limit):
        if overdraft_limit < 0:
            raise ValueError("overdraft_limit cannot be negative")
        super().__init__(owner)
        self.overdraft_limit = overdraft_limit
    ### override la withdraw cu limita de overdraft
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        if amount > self.balance + self.overdraft_limit: 
            raise ValueError("not enough balance")
        self.balance -= amount

try:
    sa = SavingsAccount("John", 0.01)
    sa.deposit(100)
    sa.add_interest()
    print(sa)

    checking_acc = CheckingAccount("Bob", 100)
    checking_acc.deposit(100)
    checking_acc.withdraw(130)
    print(checking_acc)
except ValueError as e:
    print(e)
