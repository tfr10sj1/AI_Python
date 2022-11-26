account_nbr_account_type_balance_list = {}
class Account(): 
    def __init__(self):
        global account_nbr_acount_type_balance_list
        self.account_type = "debit account" 
 
        
    def add_new_account(self, search_text, replace_text):
        account_nbr_account_type_balance_list[self.set_account_nbr()] = self.account_type +":"+str(0) + "#"
        for item in account_nbr_account_type_balance_list:
            replace_text += str(item) + ":" + str(account_nbr_account_type_balance_list[item])

        with open(r'customers.txt', 'r') as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open(r'customers.txt', 'w') as file:
            file.write(data)
            print("New account is added")
        
        return account_nbr_account_type_balance_list
    
    def show_account_info(self):
        print("Account number is: ", account_nbr)
        print(" ")
        print("Account type is: ", self.account_type)
        print(" ")
        print("Balance is: ", balance)
        
    def deposit(self, amount, search_txt, replace_txt):
        global account_nbr_acount_type_balance_list, account_nbr, balance 
        self.amount = amount
        balance += self.amount
        account_nbr_account_type_balance_list[account_nbr] = self.account_type +":"+ str(balance) + "#"
        
        with open(r'customers.txt', 'r') as file:
            data = file.read()
            data = data.replace(search_txt, replace_txt)

        with open(r'customers.txt', 'w') as file:
            file.write(data)
            
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
    
    def set_account_nbr(self):
        count = 1001
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            for line in data: 
                customer_id, name, pnr,  *accounts = line.split(":")
                for account in accounts:
                    if "#" in account and str(count+1) not in accounts:
                        count += 1
        return  count


       