account_nbr_account_type_balance_list  = {}
account_nbr = 0
balance = 0

class Account(): 
    def __init__(self):
        global account_nbr_acount_type_balance_list, account_nbr, balance 
        self.account_type = "debit account" 
        
        
    def add_new_account(self):
        self.set_account_nbr()
        account_nbr_account_type_balance_list[account_nbr] = self.account_type +":"+str(balance) + "#"
        
    def show_account_info(self):
        print("Account number is: ", account_nbr)
        print(" ")
        print("Account type is: ", self.account_type)
        print(" ")
        print("Balance is: ", balance)
        print(account_nbr_account_type_balance_list)
        
    def deposit(self, amount):
        global account_nbr_acount_type_balance_list, account_nbr, balance 
        self.amount = amount
        balance += self.amount
        account_nbr_account_type_balance_list[account_nbr] = self.account_type +":"+ str(balance) + "#"
        print("your balance is updated to: ",  balance)
       
        
    def withdraw(self, amount):
        global account_nbr_account_type_balance_list, account_nbr, balance 
        self.amount = amount
        if self.amount > balance:
            print("Invalid request! your balance is less than ", self.amount)
        else:
            balance -= self.amount
            print("your balance is updated to: ",  balance)
            account_nbr_account_type_balance_list[account_nbr] = self.account_type +":"+ str(balance) + "#"
        
    def set_account_nbr(self):
        global balance, account_nbr
        balance = 0
        if account_nbr == 0:
            account_nbr = 1001
        else:
            account_nbr +=1
        
       