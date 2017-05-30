class BankAccount:

    def __init__(self, balance, acc_name):
        self.balance = balance
        self.acc_name = acc_name

    def __str__(self):
        return 'Hello {}, your balance is {}'.format(self.acc_name, self.balance)

    def withdrawal(self, amount):
        if self.balance - amount > 0 and self.balance >= amount:
            self.balance -= amount
            print('Thank you {}. Your remaining balance is {}.'.format(self.acc_name, self.balance))
        else:
            print("Sorry, you have no money.")


    def deposit(self, amount):
        self.balace += amount
        return 'Thank you {}, your balance is {}'.format(self.acc_name, self.balance)


class BankAccountSpecial(BankAccount):
    def __init__(self, balance, acc_name):
        super().__init__(balance, acc_name)

    def withdrawal(self, amount):
        if self.balance - amount > 100 and self.balance >= amount:
            self.balance -= amount
            print('Thank you {}. Your remaining balance is {}.'.format(self.acc_name, self.balance))
        else:
            print("Sorry, not enough money in account to make withdrawal.")



acc1 = BankAccount(100, 'Conner')
print(acc1)
acc1.withdrawal(50)
