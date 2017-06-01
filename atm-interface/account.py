from random import randrange

class Account:
    balance = 0
    interest_rate = 0.001
    account_type = 'Checking'
    account_ID = 000000000

    def __init__(self):
        self.account_ID = randrange(000000000, 999999999)

    def get_funds(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False


    def withdraw(self, amount):
        try:
            if check_withdrawal(amount) == False:
                 raise ValueError
            elif self.get_standing() == False and self.balance >= amount + 15:
                self.balance = self.balance - 15 - amount
                print("Your account is in bad standing, so we charged you fifteen dollars for this transaction. ")
                return amount
            elif self.get_standing() == False and self.balance < amount + 15:
                print("Your account is in bad standing, and we would charge you fifteen dollars for this transaction, but you don't have enough cash for that so you can't make a transaction. ")
            else:
                self.balance = self.balance - amount
                return amount
        except ValueError:
            print("Not enough money for that withdrawal")

    def calc_interest(self):
        return self.balance * self. interest_rate

    def get_standing(self):
        if self.balance>=1000:
            return True
        else:
            return False


class SavingsAccount(Account):

    def __init__(self):
        self.account_ID = randrange(000000000, 999999999)
        self.account_type = 'Savings'
