class Bank:
    customer_info = {}
    def __init__(self):
        self._load()
    
    def _load(self):        
        with open("customers.txt", 'r') as file:
            data = [line.strip() for line in file]
            
        for line in data: 
            global customer_info
            customer_id, name, pnr,  *accounts = line.split(":")
            info = name + ":" + pnr
            
            for item in accounts:
                if("#" in item):
                    balance, new_account_nbr = item.split("#")
                    info += ":" + balance + "#" + new_account_nbr
                else:
                    info += ":" + str(item)
                    
            self.customer_info[customer_id] = info 
            
    def get_customers(self):
        for key in self.customer_info: 
            name, pnr,  *accounts = self.customer_info[key].split(":")
            print(name, pnr)
            
    def add_customer(name, pnr):
        "add customer"
    def get_customer(self, pnr):
        for i in self.customer_info:
            if str(pnr) in self.customer_info[i]:
                name, pnr,  *accounts = self.customer_info[i].split(":")
                print(name, pnr, i, accounts)
                
    def change_customer_name(name, pnr):
        ""
    def remove_customer(pnr):
        ""
    def add_account(pnr):
        ""
    def get_account(pnr, account_id):
        ""
    def deposit(pnr, account_id, amount):
        balance = balance +  amount
        print("The balance is: ", balance)

    def withdraw(pnr, account_id, amount):
        ""
    def close_account(pnr, account_id):
        ""
    def get_all_transactions_by_pnr_acc_nr( pnr, acc_nr ):
        "VG"
    
