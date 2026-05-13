from account import Account
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate, withdrawal_limit=100):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.__balance += interest
        print(f'An interest of {interest} has been deposited to your account.\n Balance: {self.get_balance()}')


    def withdraw(self, amount):
        if 0< amount <= self.withdrawal_limit:
            self.__balance -= amount
            print(f'{amount} has been withdrawn from your savings account.\nBalance: ${self.get_balance()}')
            self.withdrawal_limit -= amount
        elif 0>= amount <= self.withdrawal_limit:
            print(f'Withdrawal amount must be greater than $0 and should not exceed the limit of ${self.withdrawal_limit}.')
        elif 0< amount > self.withdrawal_limit:
            print(f'You cannot withdraw more than ${self.withdrawal_limit} from your savings account.')

print('--- Savings Account ---')
savings = SavingsAccount("Billy", 100000, 0.05, 100)
print(f'Your current balance is {savings.get_balance()}')
savings.deposit(100)
savings.apply_interest()
print(savings.get_balance())
savings.withdraw(100)
savings.withdraw(200)
savings.apply_interest()
print(savings.get_balance())