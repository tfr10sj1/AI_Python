account_nbr_account_type_balance_list = {}
account_nbr = 0
balance = 0

class Account(): 
    def __init__(self):
        global account_nbr_acount_type_balance_list, account_nbr, balance 
        self.account_type = "debit account" 
        
        
    def add_new_account(self):
        self.set_account_nbr()
        account_nbr_account_type_balance_list[account_nbr] = self.account_type +":"+str(balance) + "#"
        return account_nbr_account_type_balance_list
    
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
        return account_nbr_account_type_balance_list
        
    def withdraw(self, amount):
        global account_nbr_account_type_balance_list, account_nbr, balance 
        self.amount = amount
        if self.amount > balance:
            print("Invalid request! your balance is less than ", self.amount)
        else:
            balance -= self.amount
            print("your balance is updated to: ",  balance)
            account_nbr_account_type_balance_list[account_nbr] = self.account_type +":"+ str(balance) + "#"
        return account_nbr_account_type_balance_list
    
    def set_account_nbr(self, forced_account_nbr = None):
        global balance, account_nbr
        count = 1001
        self.forced_account_nbr = forced_account_nbr
        
        if forced_account_nbr == None:
            with open("customers.txt", 'r') as file:
                data = [line.strip() for line in file]
                for line in data: 
                    customer_id, name, pnr,  *accounts = line.split(":")
                    for account in accounts:
                        if "#" in account:
                            count += 2
                balance = 0
                account_nbr = count
        else:   
            account_nbr = forced_account_nbr


       