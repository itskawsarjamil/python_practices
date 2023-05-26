class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=10000
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            return f'No money for you.Minimum withdraw:{self.min_withdraw}'
        elif amount>self.max_withdraw:
            return f"You can't withdraw more than {self.max_withdraw}"
        elif amount>self.balance:
            return f"You have not enough money"
        else:
            self.balance-=amount
            return f"Money withdraw successfull"
    
    def deposit(self,amount):
        self.balance=self.balance+amount

my_bank=Bank(5000)
reply=my_bank.withdraw(800)
print(reply)
print(my_bank.get_balance())
my_bank.deposit(5000)
print(my_bank.get_balance())