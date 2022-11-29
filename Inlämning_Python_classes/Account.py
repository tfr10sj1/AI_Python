accounts = {}

class Account(): 
    def __init__(self, account_nbr, balance):
        self.account_nbr = account_nbr
        if self.check_if_account_nbr_not_exist(self.account_nbr):
            self.balance = balance
            self.update_values(self.account_nbr)
            print("Account and balans are added!")
        else:
            print("Choose another Account_nbr!")
        
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        self.update_values(self.account_nbr)
        print("your balance is updated to: ", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Invalid request! your balance is less than ", self.amount)
        else:
            self.balance -= self.amount
            self.update_values(self.account_nbr)
            print("your balance is updated to: ",  self.balance)
            
    def check_if_account_nbr_not_exist(self, account_nbr):
        global accounts
        print(accounts, self.account_nbr)
        if account_nbr not in accounts:
            print( str(account_nbr) + " is new one!")
            return True
        else:
            print(str(account_nbr) + " already exists!")
            return False
        
    def update_values(self, account_type):
        global accounts
        accounts[self.account_nbr] = ":" + "debit account" + ":" + str(self.balance) + "#"
        
    def get_accounts(self):
        global accounts
        return accounts
    
    def show_account_info(self, Searched_account_nbr):
        global accounts
        x = ["account_nbr", "account_type", "balance"]
        y = [account for account in accounts if account in accounts[account]]
        for account in accounts:
            if str(Searched_account_nbr) == str(account):
                temp1, account_type, balance = accounts[account].split(":")
                pure_balance, temp2 = balance.split("#")
                print("Account number is: ", account)
                print(" ")
                print("Account type is: ", account_type)
                print(" ")
                print("Balance is: ", pure_balance)
