class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'${amount} has been added to your account.\nBalance: {self.get_balance()}')
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'You have withdrawn ${amount}. New balance is ${self.__balance}.')
        else :
            print("You don't have enough money to withdraw.")






