class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def showBalance(self):
        return self.balance

class BankAccountWithLimit(BankAccount):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def withdrawal(self, amount):
        if self.balance - amount >= self.limit:
            super().withdrawal(amount)
        else:
            print("Insufficient funds")



# Do not remove the following lines
if __name__ == '__main__':
  account = BankAccount()

  d1 = int(input())
  d2 = int(input())
  account.deposit(d1)
  account.deposit(d2)

  w1 = int(input())
  w2 = int(input())
  w3 = int(input())
  account.withdrawal(w1)
  account.withdrawal(w2)
  account.withdrawal(w3)

  print(account.showBalance());
