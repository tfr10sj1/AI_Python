class Account(): 
    def __init__(self, account_nbr, balance):
        self.account_nbr = account_nbr
        self.balance = balance
        self.account_type = "debit account"
        
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("your balance is updated to: ", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Invalid request! your balance is less than ", self.amount)
        else:
            self.balance -= self.amount
            print("your balance is updated to: ",  self.balance)
            
    def get_account(self):
        account = str(self.account_nbr) + ":" + self.account_type + ":" + str(self.balance) + "#"
        return account
    
    def show_account_info(self):
        print("Account number is: ", self.account_nbr)
        print(" ")
        print("Account type is: ", self.account_type)
        print(" ")
        print("Balance is: ", self.balance)
        
